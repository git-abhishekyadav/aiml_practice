import graphviz

g = graphviz.Digraph('erd', format='png')
g.attr(rankdir='LR', splines='ortho', nodesep='0.6', ranksep='1.1',
       bgcolor='white', fontname='Helvetica')
g.attr('node', shape='plain', fontname='Helvetica')
g.attr('edge', fontname='Helvetica', fontsize='10', color='#5f6b7a',
       fontcolor='#5f6b7a')

HEADER_BG = '#1f2d3d'
PK_COLOR = '#b8860b'
FK_COLOR = '#1d6fa5'

def row(port, name, dtype, key=''):
    if key == 'PK':
        namecell = f'<FONT COLOR="{PK_COLOR}"><B>🔑 {name}</B></FONT>'
    elif key == 'PK/FK':
        namecell = f'<FONT COLOR="{PK_COLOR}"><B>🔑 {name}</B></FONT>'
    elif key == 'FK':
        namecell = f'<FONT COLOR="{FK_COLOR}">{name}</FONT>'
    else:
        namecell = name
    tag = key if key else ''
    return (f'<TR><TD ALIGN="LEFT" PORT="{port}" BGCOLOR="white">{namecell}</TD>'
            f'<TD ALIGN="LEFT" BGCOLOR="white"><FONT COLOR="#5f6b7a">{dtype}</FONT></TD>'
            f'<TD ALIGN="LEFT" BGCOLOR="white"><FONT COLOR="#94a0ad" POINT-SIZE="9">{tag}</FONT></TD></TR>')

def table(title, rows):
    body = ''.join(rows)
    return (f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="6" '
            f'COLOR="#c9ced4">'
            f'<TR><TD COLSPAN="3" BGCOLOR="{HEADER_BG}"><FONT COLOR="white"><B>{title}</B></FONT></TD></TR>'
            f'{body}</TABLE>>')

entities = {
    'parties': table('parties', [
        row('id', 'id', 'UUID', 'PK'),
        row('name', 'name', 'VARCHAR'),
        row('party_type', 'party_type', 'VARCHAR'),
    ]),
    'assets': table('assets', [
        row('id', 'id', 'UUID', 'PK'),
        row('current_owner_id', 'current_owner_id', 'UUID', 'FK'),
        row('asset_type', 'asset_type', 'VARCHAR'),
        row('label', 'label', 'VARCHAR'),
        row('status', 'status', 'VARCHAR'),
    ]),
    'asset_specs': table('asset_specs', [
        row('asset_id', 'asset_id', 'UUID', 'PK/FK'),
        row('coat_color', 'coat_color', 'VARCHAR'),
        row('coat_pattern', 'coat_pattern', 'VARCHAR'),
        row('height_hands', 'height_hands', 'NUMERIC'),
        row('weight', 'weight', 'NUMERIC'),
    ]),
    'asset_identifiers': table('asset_identifiers', [
        row('id', 'id', 'UUID', 'PK'),
        row('asset_id', 'asset_id', 'UUID', 'FK'),
        row('id_type', 'id_type', 'VARCHAR'),
        row('value', 'value', 'VARCHAR'),
        row('issuing_authority', 'issuing_authority', 'VARCHAR'),
        row('verified_at', 'verified_at', 'DATE'),
        row('is_primary', 'is_primary', 'BOOLEAN'),
    ]),
    'asset_lineage': table('asset_lineage', [
        row('id', 'id', 'UUID', 'PK'),
        row('asset_id', 'asset_id', 'UUID', 'FK'),
        row('related_asset_id', 'related_asset_id', 'UUID', 'FK'),
        row('relation_type', 'relation_type', 'VARCHAR'),
    ]),
    'registry_enrollments': table('registry_enrollments', [
        row('id', 'id', 'UUID', 'PK'),
        row('asset_id', 'asset_id', 'UUID', 'FK'),
        row('breed_standard', 'breed_standard', 'VARCHAR'),
        row('status', 'status', 'VARCHAR'),
        row('evaluated_attributes', 'evaluated_attributes', 'JSONB'),
        row('evaluated_by', 'evaluated_by', 'VARCHAR'),
        row('effective_date', 'effective_date', 'DATE'),
    ]),
    'lifecycle_events': table('lifecycle_events', [
        row('id', 'id', 'UUID', 'PK'),
        row('asset_id', 'asset_id', 'UUID', 'FK'),
        row('event_type', 'event_type', 'VARCHAR'),
        row('event_date', 'event_date', 'DATE'),
    ]),
    'ownership_transfers': table('ownership_transfers', [
        row('event_id', 'event_id', 'UUID', 'PK/FK'),
        row('from_owner_id', 'from_owner_id', 'UUID', 'FK'),
        row('to_owner_id', 'to_owner_id', 'UUID', 'FK'),
        row('sale_price', 'sale_price', 'NUMERIC'),
    ]),
    'documents': table('documents', [
        row('id', 'id', 'UUID', 'PK'),
        row('asset_id', 'asset_id', 'UUID', 'FK'),
        row('linked_event_id', 'linked_event_id', 'UUID', 'FK'),
        row('doc_type', 'doc_type', 'VARCHAR'),
        row('file_url', 'file_url', 'TEXT'),
        row('issued_by', 'issued_by', 'VARCHAR'),
        row('verified', 'verified', 'BOOLEAN'),
    ]),
}

for nid, label in entities.items():
    g.node(nid, label=label)

def edge(src, src_port, dst, dst_port, label, card):
    # card: 'one_many' or 'one_one' or 'one_zero_many'
    if card == 'one_many':
        arrowtail, arrowhead = 'tee', 'crow'
    elif card == 'one_zero_many':
        arrowtail, arrowhead = 'tee', 'odot'
    else:  # one_one
        arrowtail, arrowhead = 'tee', 'tee'
    g.edge(f'{src}:{src_port}:e', f'{dst}:{dst_port}:w',
           dir='both', arrowtail=arrowtail, arrowhead=arrowhead,
           label=label)

edge('parties', 'id', 'assets', 'current_owner_id', 'owns', 'one_many')
edge('assets', 'id', 'asset_specs', 'asset_id', 'has specs', 'one_one')
edge('assets', 'id', 'asset_identifiers', 'asset_id', 'has', 'one_many')
edge('assets', 'id', 'asset_lineage', 'asset_id', 'is child in', 'one_many')
edge('assets', 'id', 'asset_lineage', 'related_asset_id', 'is sire/dam in', 'one_many')
edge('assets', 'id', 'registry_enrollments', 'asset_id', 'enrolled in', 'one_many')
edge('assets', 'id', 'lifecycle_events', 'asset_id', 'has', 'one_many')
edge('lifecycle_events', 'id', 'ownership_transfers', 'event_id', 'detail', 'one_zero_many')
edge('parties', 'id', 'ownership_transfers', 'from_owner_id', 'sold by', 'one_many')
edge('parties', 'id', 'ownership_transfers', 'to_owner_id', 'sold to', 'one_many')
edge('assets', 'id', 'documents', 'asset_id', 'has', 'one_many')
edge('lifecycle_events', 'id', 'documents', 'linked_event_id', 'supports', 'one_zero_many')

g.attr(label='Livestock / Asset Registry — Entity-Relationship Diagram', labelloc='t',
       fontsize='18', fontcolor='#1f2d3d')
g.render('/home/abhishek/Desktop/Github/aiml_practice/asset_registry_erd',
         format='png',
         cleanup=True)
g.render('/home/abhishek/Desktop/Github/aiml_practice/asset_registry_erd',
         format='svg',
         cleanup=True)
print('done')
