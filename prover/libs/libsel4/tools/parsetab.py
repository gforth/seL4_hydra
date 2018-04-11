
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'C2CEC69EFFA71B3AC74F9139DF3D7D64'
    
_lr_action_items = {'TAG':([20,25,32,44,45,],[-21,-19,39,-22,-20,]),'LBRACE':([10,13,15,24,],[-9,17,20,-10,]),'RPAREN':([14,18,19,26,31,],[-11,-12,24,34,-13,]),'RBRACE':([17,20,22,25,32,35,41,42,44,45,],[-14,-21,27,-19,38,-17,-15,-16,-22,-20,]),'FIELD_HIGH':([17,22,35,41,42,],[-14,30,-17,-15,-16,]),'MASK':([20,25,44,],[-21,33,-22,]),'PADDING':([17,22,35,41,42,],[-14,28,-17,-15,-16,]),'FIELD':([17,22,35,41,42,],[-14,29,-17,-15,-16,]),'BASE':([0,2,5,7,8,9,27,34,38,],[-2,3,-3,-5,-4,-6,-8,-7,-18,]),'COMMA':([14,16,18,19,31,],[-11,21,-12,23,-13,]),'LPAREN':([9,10,],[12,14,]),'INTLIT':([3,12,21,28,33,36,37,40,43,],[9,16,26,35,40,41,42,44,45,]),'IDENTIFIER':([4,6,11,14,23,29,30,39,],[10,11,15,18,31,36,37,43,]),'TAGGED_UNION':([0,2,5,7,8,9,27,34,38,],[-2,6,-3,-5,-4,-6,-8,-7,-18,]),'BLOCK':([0,2,5,7,8,9,27,34,38,],[-2,4,-3,-5,-4,-6,-8,-7,-18,]),'$end':([0,1,2,5,7,8,9,27,34,38,],[-2,0,-1,-3,-5,-4,-6,-8,-7,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'entity_list':([0,],[2,]),'fields':([17,],[22,]),'opt_visible_order_spec':([10,],[13,]),'masks':([20,],[25,]),'start':([0,],[1,]),'base':([2,],[5,]),'visible_order_spec':([14,],[19,]),'tags':([25,],[32,]),'tagged_union':([2,],[7,]),'block':([2,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> entity_list','start',1,'p_start','bitfield_gen.py',105),
  ('entity_list -> <empty>','entity_list',0,'p_entity_list_empty','bitfield_gen.py',109),
  ('entity_list -> entity_list base','entity_list',2,'p_entity_list_base','bitfield_gen.py',113),
  ('entity_list -> entity_list block','entity_list',2,'p_entity_list_block','bitfield_gen.py',120),
  ('entity_list -> entity_list tagged_union','entity_list',2,'p_entity_list_union','bitfield_gen.py',126),
  ('base -> BASE INTLIT','base',2,'p_base_simple','bitfield_gen.py',132),
  ('base -> BASE INTLIT LPAREN INTLIT COMMA INTLIT RPAREN','base',7,'p_base_mask','bitfield_gen.py',136),
  ('block -> BLOCK IDENTIFIER opt_visible_order_spec LBRACE fields RBRACE','block',6,'p_block','bitfield_gen.py',140),
  ('opt_visible_order_spec -> <empty>','opt_visible_order_spec',0,'p_opt_visible_order_spec_empty','bitfield_gen.py',145),
  ('opt_visible_order_spec -> LPAREN visible_order_spec RPAREN','opt_visible_order_spec',3,'p_opt_visible_order_spec','bitfield_gen.py',149),
  ('visible_order_spec -> <empty>','visible_order_spec',0,'p_visible_order_spec_empty','bitfield_gen.py',153),
  ('visible_order_spec -> IDENTIFIER','visible_order_spec',1,'p_visible_order_spec_single','bitfield_gen.py',157),
  ('visible_order_spec -> visible_order_spec COMMA IDENTIFIER','visible_order_spec',3,'p_visible_order_spec','bitfield_gen.py',161),
  ('fields -> <empty>','fields',0,'p_fields_empty','bitfield_gen.py',165),
  ('fields -> fields FIELD IDENTIFIER INTLIT','fields',4,'p_fields_field','bitfield_gen.py',169),
  ('fields -> fields FIELD_HIGH IDENTIFIER INTLIT','fields',4,'p_fields_field_high','bitfield_gen.py',173),
  ('fields -> fields PADDING INTLIT','fields',3,'p_fields_padding','bitfield_gen.py',177),
  ('tagged_union -> TAGGED_UNION IDENTIFIER IDENTIFIER LBRACE masks tags RBRACE','tagged_union',7,'p_tagged_union','bitfield_gen.py',181),
  ('tags -> <empty>','tags',0,'p_tags_empty','bitfield_gen.py',186),
  ('tags -> tags TAG IDENTIFIER INTLIT','tags',4,'p_tags','bitfield_gen.py',190),
  ('masks -> <empty>','masks',0,'p_masks_empty','bitfield_gen.py',194),
  ('masks -> masks MASK INTLIT INTLIT','masks',4,'p_masks','bitfield_gen.py',198),
]
