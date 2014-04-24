
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\n\x06L|k\x16_\x90\x1eC!(f\xc8\x03\xed'
    
_lr_action_items = {'DTYPE_PART2':([13,18,],[25,31,]),'DTYPE_PART1':([6,],[13,]),'NUMBER':([26,32,45,51,],[37,37,37,37,]),'FOREIGN':([60,],[65,]),'REFERENCES':([80,],[81,]),'NULL':([12,14,16,17,18,25,27,30,31,39,40,43,44,52,54,59,62,],[-14,-13,-12,-39,-15,-19,40,-22,-18,-25,-24,52,-21,-23,-16,-20,-17,]),'ALTER':([2,7,8,19,20,21,23,34,56,],[-39,-3,-39,35,-2,-28,-4,-27,-29,]),'RPAREN':([12,14,16,17,18,25,27,30,31,37,39,40,44,46,52,53,54,58,59,62,66,69,70,73,75,76,77,78,84,],[-14,-13,-12,28,-15,-19,41,-22,-18,-26,-25,-24,-21,54,-23,59,-16,62,-20,-17,-39,74,-36,-38,-35,79,80,-37,85,]),'SEMICOLON':([5,10,11,24,28,29,41,42,48,49,74,79,85,],[-39,-6,23,-5,-10,-8,-11,-9,56,-33,-34,-31,-32,]),'CONSTRAINT':([47,],[55,]),'CREATE':([0,2,7,8,20,23,],[3,-39,-3,3,-2,-4,]),'COMMA':([12,14,16,17,18,25,27,30,31,37,38,39,40,44,52,54,59,62,73,],[-14,-13,-12,29,-15,-19,42,-22,-18,-26,51,-25,-24,-21,-23,-16,-20,-17,78,]),'TABLE':([3,35,],[9,50,]),'IDENTIFIER':([1,5,9,10,11,24,28,29,36,41,42,55,57,66,69,70,71,72,73,75,78,81,83,],[6,-39,22,-6,6,-5,-10,-8,-7,-11,-9,60,61,-39,73,-36,76,77,-38,-35,-37,82,84,]),'DTYPE_BOTH_1PARAM':([6,],[18,]),'$end':([2,4,7,8,19,20,21,23,34,56,],[-39,0,-3,-39,-1,-2,-28,-4,-27,-29,]),'DTYPE_SOLO':([6,],[12,]),'DTYPE_SOLO_1PARAM2':([6,],[15,]),'ADD':([33,61,],[47,-30,]),'LPAREN':([15,18,22,31,63,67,68,82,],[26,32,36,45,66,71,72,83,]),'UNIQUE':([12,14,16,17,18,25,27,30,31,39,40,44,52,54,59,60,62,],[-14,-13,-12,-39,-15,-19,39,-22,-18,-25,-24,-21,-23,-16,-20,63,-17,]),'PRIMARY':([60,],[64,]),'ONLY':([50,],[57,]),'KEY':([64,65,],[67,68,]),'NOT':([12,14,16,17,18,25,27,30,31,39,40,44,52,54,59,62,],[-14,-13,-12,-39,-15,-19,43,-22,-18,-25,-24,-21,-23,-16,-20,-17,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tableHeader':([0,8,],[1,1,]),'constraintPart':([17,],[27,]),'multi_params':([66,],[69,]),'moreAlterBlocks':([8,],[19,]),'tableBlock':([0,8,],[2,20,]),'moreAttributes':([5,],[11,]),'dtypeTwopart':([6,],[14,]),'parameter':([26,32,45,51,],[38,46,53,58,]),'moreBlocks':([2,],[8,]),'dtypeSolo':([6,],[16,]),'dtypes':([6,],[17,]),'multi_1param':([69,],[75,]),'alterHeader':([19,],[33,]),'attributeBlock':([1,11,],[5,24,]),'multi_attr_constr':([33,],[49,]),'alterBlock':([19,],[34,]),'root':([0,],[4,]),'alterBody':([33,],[48,]),'empty':([2,5,8,17,66,],[7,10,21,30,70,]),'constraints':([27,],[44,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> tableBlock moreBlocks moreAlterBlocks','root',3,'p_root','/home/re/sql-data-farmer/Harvester/lex_parse.py',204),
  ('moreBlocks -> moreBlocks tableBlock','moreBlocks',2,'p_moreBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',209),
  ('moreBlocks -> empty','moreBlocks',1,'p_moreBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',210),
  ('tableBlock -> tableHeader attributeBlock moreAttributes SEMICOLON','tableBlock',4,'p_tableBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',220),
  ('moreAttributes -> moreAttributes attributeBlock','moreAttributes',2,'p_moreAttributes','/home/re/sql-data-farmer/Harvester/lex_parse.py',225),
  ('moreAttributes -> empty','moreAttributes',1,'p_moreAttributes','/home/re/sql-data-farmer/Harvester/lex_parse.py',226),
  ('tableHeader -> CREATE TABLE IDENTIFIER LPAREN','tableHeader',4,'p_tableHeader','/home/re/sql-data-farmer/Harvester/lex_parse.py',231),
  ('attributeBlock -> IDENTIFIER dtypes COMMA','attributeBlock',3,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',244),
  ('attributeBlock -> IDENTIFIER dtypes constraintPart COMMA','attributeBlock',4,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',245),
  ('attributeBlock -> IDENTIFIER dtypes RPAREN','attributeBlock',3,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',246),
  ('attributeBlock -> IDENTIFIER dtypes constraintPart RPAREN','attributeBlock',4,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',247),
  ('dtypes -> dtypeSolo','dtypes',1,'p_dtypes','/home/re/sql-data-farmer/Harvester/lex_parse.py',259),
  ('dtypes -> dtypeTwopart','dtypes',1,'p_dtypes','/home/re/sql-data-farmer/Harvester/lex_parse.py',260),
  ('dtypeSolo -> DTYPE_SOLO','dtypeSolo',1,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',274),
  ('dtypeSolo -> DTYPE_BOTH_1PARAM','dtypeSolo',1,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',275),
  ('dtypeSolo -> DTYPE_BOTH_1PARAM LPAREN parameter RPAREN','dtypeSolo',4,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',276),
  ('dtypeSolo -> DTYPE_SOLO_1PARAM2 LPAREN parameter COMMA parameter RPAREN','dtypeSolo',6,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',277),
  ('dtypeTwopart -> DTYPE_BOTH_1PARAM DTYPE_PART2','dtypeTwopart',2,'p_dtypeTwopart','/home/re/sql-data-farmer/Harvester/lex_parse.py',295),
  ('dtypeTwopart -> DTYPE_PART1 DTYPE_PART2','dtypeTwopart',2,'p_dtypeTwopart','/home/re/sql-data-farmer/Harvester/lex_parse.py',296),
  ('dtypeTwopart -> DTYPE_BOTH_1PARAM DTYPE_PART2 LPAREN parameter RPAREN','dtypeTwopart',5,'p_dtypeTwopart','/home/re/sql-data-farmer/Harvester/lex_parse.py',297),
  ('constraintPart -> constraintPart constraints','constraintPart',2,'p_constraintPart','/home/re/sql-data-farmer/Harvester/lex_parse.py',311),
  ('constraintPart -> empty','constraintPart',1,'p_constraintPart','/home/re/sql-data-farmer/Harvester/lex_parse.py',312),
  ('constraints -> NOT NULL','constraints',2,'p_constraints','/home/re/sql-data-farmer/Harvester/lex_parse.py',317),
  ('constraints -> NULL','constraints',1,'p_constraints','/home/re/sql-data-farmer/Harvester/lex_parse.py',318),
  ('constraints -> UNIQUE','constraints',1,'p_constraints','/home/re/sql-data-farmer/Harvester/lex_parse.py',319),
  ('parameter -> NUMBER','parameter',1,'p_parameter','/home/re/sql-data-farmer/Harvester/lex_parse.py',335),
  ('moreAlterBlocks -> moreAlterBlocks alterBlock','moreAlterBlocks',2,'p_moreAlterBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',345),
  ('moreAlterBlocks -> empty','moreAlterBlocks',1,'p_moreAlterBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',346),
  ('alterBlock -> alterHeader alterBody SEMICOLON','alterBlock',3,'p_alterBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',352),
  ('alterHeader -> ALTER TABLE ONLY IDENTIFIER','alterHeader',4,'p_alterHeader','/home/re/sql-data-farmer/Harvester/lex_parse.py',358),
  ('alterBody -> ADD CONSTRAINT IDENTIFIER PRIMARY KEY LPAREN IDENTIFIER RPAREN','alterBody',8,'p_alterBody','/home/re/sql-data-farmer/Harvester/lex_parse.py',370),
  ('alterBody -> ADD CONSTRAINT IDENTIFIER FOREIGN KEY LPAREN IDENTIFIER RPAREN REFERENCES IDENTIFIER LPAREN IDENTIFIER RPAREN','alterBody',13,'p_alterBody','/home/re/sql-data-farmer/Harvester/lex_parse.py',371),
  ('alterBody -> multi_attr_constr','alterBody',1,'p_alterBody','/home/re/sql-data-farmer/Harvester/lex_parse.py',372),
  ('multi_attr_constr -> ADD CONSTRAINT IDENTIFIER UNIQUE LPAREN multi_params RPAREN','multi_attr_constr',7,'p_multi_attr_constr','/home/re/sql-data-farmer/Harvester/lex_parse.py',426),
  ('multi_params -> multi_params multi_1param','multi_params',2,'p_multi_params','/home/re/sql-data-farmer/Harvester/lex_parse.py',431),
  ('multi_params -> empty','multi_params',1,'p_multi_params','/home/re/sql-data-farmer/Harvester/lex_parse.py',432),
  ('multi_1param -> IDENTIFIER COMMA','multi_1param',2,'p_multi_1param','/home/re/sql-data-farmer/Harvester/lex_parse.py',437),
  ('multi_1param -> IDENTIFIER','multi_1param',1,'p_multi_1param','/home/re/sql-data-farmer/Harvester/lex_parse.py',438),
  ('empty -> <empty>','empty',0,'p_empty','/home/re/sql-data-farmer/Harvester/lex_parse.py',469),
]
