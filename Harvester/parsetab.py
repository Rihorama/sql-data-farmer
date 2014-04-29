
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = "\xad\xb6W{nA'&\xd4=\x8c\x80R\x8f\xe7\x94"
    
_lr_action_items = {'DTYPE_PART2':([13,20,],[29,39,]),'DTYPE_PART1':([6,],[13,]),'NUMBER':([31,38,40,48,59,70,],[49,49,49,68,49,49,]),'FOREIGN':([84,],[91,]),'LBRACKET':([12,14,15,16,17,20,27,28,29,30,32,39,47,67,69,72,73,75,80,83,87,93,],[-52,-52,-17,-15,-52,-16,48,-28,-22,48,48,-21,-27,-29,-19,-25,-24,-18,-30,-23,-20,-26,]),'REFERENCES':([111,],[113,]),'NULL':([12,14,15,16,17,18,20,27,28,29,30,32,33,36,39,47,51,52,55,56,67,69,71,72,73,75,80,83,87,93,],[-52,-52,-17,-15,-52,-52,-16,-14,-28,-22,-13,-12,52,-32,-21,-27,-35,-34,71,-31,-29,-19,-33,-25,-24,-18,-30,-23,-20,-26,]),'ALTER':([2,7,8,21,22,23,25,42,45,46,66,77,112,],[-52,-3,-52,43,-2,-41,-52,-40,-4,-38,-37,-42,-39,]),'RPAREN':([12,14,15,16,17,18,20,27,28,29,30,32,33,36,39,47,49,50,51,52,56,58,60,67,69,71,72,73,74,75,80,81,83,87,93,94,98,99,103,105,106,107,109,116,],[-52,-52,-17,-15,-52,34,-16,-14,-28,-22,-13,-12,53,-32,-21,-27,-36,69,-35,-34,-31,73,75,-29,-19,-33,-25,-24,83,-18,-30,87,-23,-20,-26,-52,104,-49,-51,-48,110,111,-50,117,]),'SEMICOLON':([5,10,11,26,34,35,53,54,62,63,104,108,110,117,],[-52,25,-6,-5,-10,-8,-11,-9,77,-46,-47,112,-44,-45,]),'CONSTRAINT':([61,],[76,]),'CREATE':([0,2,7,8,22,25,45,46,66,112,],[3,-52,-3,3,-2,-52,-4,-38,-37,-39,]),'SEQUENCE':([25,45,46,66,112,],[-52,65,-38,-37,-39,]),'BY':([86,],[92,]),'DTYPE_TIMEZONE_PARAM':([6,37,82,],[19,57,88,]),'TABLE':([3,43,],[9,64,]),'IDENTIFIER':([1,5,9,10,11,19,26,34,35,44,53,54,57,65,73,76,78,88,92,94,98,99,100,101,102,103,105,109,113,115,],[6,-52,24,6,-6,37,-5,-10,-8,-7,-11,-9,72,79,82,84,85,93,97,-52,103,-49,106,107,108,-51,-48,-50,114,116,]),'DTYPE_BOTH_1PARAM':([6,],[20,]),'$end':([2,4,7,8,21,22,23,25,42,45,46,66,77,112,],[-52,0,-3,-52,-1,-2,-41,-52,-40,-4,-38,-37,-42,-39,]),'DTYPE_SOLO':([6,],[16,]),'DTYPE_SOLO_1PARAM2':([6,],[15,]),'PERIOD':([97,],[102,]),'ADD':([41,85,],[61,-43,]),'LPAREN':([15,19,20,24,39,89,95,96,114,],[31,38,40,44,59,94,100,101,115,]),'UNIQUE':([12,14,15,16,17,18,20,27,28,29,30,32,33,36,39,47,51,52,56,67,69,71,72,73,75,80,83,84,87,93,],[-52,-52,-17,-15,-52,-52,-16,-14,-28,-22,-13,-12,51,-32,-21,-27,-35,-34,-31,-29,-19,-33,-25,-24,-18,-30,-23,89,-20,-26,]),'PRIMARY':([84,],[90,]),'OWNED':([79,],[86,]),'ONLY':([64,],[78,]),'KEY':([90,91,],[95,96,]),'NOT':([12,14,15,16,17,18,20,27,28,29,30,32,33,36,39,47,51,52,56,67,69,71,72,73,75,80,83,87,93,],[-52,-52,-17,-15,-52,-52,-16,-14,-28,-22,-13,-12,55,-32,-21,-27,-35,-34,-31,-29,-19,-33,-25,-24,-18,-30,-23,-20,-26,]),'RBRACKET':([48,68,],[67,80,]),'COMMA':([12,14,15,16,17,18,20,27,28,29,30,32,33,36,39,47,49,50,51,52,56,67,69,71,72,73,75,80,83,87,93,103,],[-52,-52,-17,-15,-52,35,-16,-14,-28,-22,-13,-12,54,-32,-21,-27,-36,70,-35,-34,-31,-29,-19,-33,-25,-24,-18,-30,-23,-20,-26,109,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'dtypeTimezone':([6,],[12,]),'multi_params':([94,],[98,]),'dtypeTwopart':([6,],[14,]),'multi_1param':([98,],[105,]),'alterBlock':([21,],[42,]),'moreDimensions':([12,14,17,],[27,30,32,]),'tableHeader':([0,8,],[1,1,]),'moreBlocks':([2,],[8,]),'sequenceBlock':([45,],[66,]),'alterBody':([41,],[62,]),'parameter':([31,38,40,59,70,],[50,58,60,74,81,]),'multi_attr_constr':([41,],[63,]),'constraintPart':([18,],[33,]),'oneDimension':([27,30,32,],[47,47,47,]),'tableBlock':([0,8,],[2,22,]),'moreAttributes':([5,],[10,]),'dtypes':([6,],[18,]),'attributeBlock':([1,10,],[5,26,]),'moreSequenceBlocks':([25,],[45,]),'moreAlterBlocks':([8,],[21,]),'dtypeSolo':([6,],[17,]),'alterHeader':([21,],[41,]),'empty':([2,5,8,12,14,17,18,25,94,],[7,11,23,28,28,28,36,46,99,]),'root':([0,],[4,]),'constraints':([33,],[56,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> tableBlock moreBlocks moreAlterBlocks','root',3,'p_root','/home/re/sql-data-farmer/Harvester/lex_parse.py',223),
  ('moreBlocks -> moreBlocks tableBlock','moreBlocks',2,'p_moreBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',228),
  ('moreBlocks -> empty','moreBlocks',1,'p_moreBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',229),
  ('tableBlock -> tableHeader attributeBlock moreAttributes SEMICOLON moreSequenceBlocks','tableBlock',5,'p_tableBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',239),
  ('moreAttributes -> moreAttributes attributeBlock','moreAttributes',2,'p_moreAttributes','/home/re/sql-data-farmer/Harvester/lex_parse.py',244),
  ('moreAttributes -> empty','moreAttributes',1,'p_moreAttributes','/home/re/sql-data-farmer/Harvester/lex_parse.py',245),
  ('tableHeader -> CREATE TABLE IDENTIFIER LPAREN','tableHeader',4,'p_tableHeader','/home/re/sql-data-farmer/Harvester/lex_parse.py',250),
  ('attributeBlock -> IDENTIFIER dtypes COMMA','attributeBlock',3,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',264),
  ('attributeBlock -> IDENTIFIER dtypes constraintPart COMMA','attributeBlock',4,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',265),
  ('attributeBlock -> IDENTIFIER dtypes RPAREN','attributeBlock',3,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',266),
  ('attributeBlock -> IDENTIFIER dtypes constraintPart RPAREN','attributeBlock',4,'p_attributeBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',267),
  ('dtypes -> dtypeSolo moreDimensions','dtypes',2,'p_dtypes','/home/re/sql-data-farmer/Harvester/lex_parse.py',279),
  ('dtypes -> dtypeTwopart moreDimensions','dtypes',2,'p_dtypes','/home/re/sql-data-farmer/Harvester/lex_parse.py',280),
  ('dtypes -> dtypeTimezone moreDimensions','dtypes',2,'p_dtypes','/home/re/sql-data-farmer/Harvester/lex_parse.py',281),
  ('dtypeSolo -> DTYPE_SOLO','dtypeSolo',1,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',309),
  ('dtypeSolo -> DTYPE_BOTH_1PARAM','dtypeSolo',1,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',310),
  ('dtypeSolo -> DTYPE_SOLO_1PARAM2','dtypeSolo',1,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',311),
  ('dtypeSolo -> DTYPE_BOTH_1PARAM LPAREN parameter RPAREN','dtypeSolo',4,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',312),
  ('dtypeSolo -> DTYPE_SOLO_1PARAM2 LPAREN parameter RPAREN','dtypeSolo',4,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',313),
  ('dtypeSolo -> DTYPE_SOLO_1PARAM2 LPAREN parameter COMMA parameter RPAREN','dtypeSolo',6,'p_dtypeSolo','/home/re/sql-data-farmer/Harvester/lex_parse.py',314),
  ('dtypeTwopart -> DTYPE_BOTH_1PARAM DTYPE_PART2','dtypeTwopart',2,'p_dtypeTwopart','/home/re/sql-data-farmer/Harvester/lex_parse.py',338),
  ('dtypeTwopart -> DTYPE_PART1 DTYPE_PART2','dtypeTwopart',2,'p_dtypeTwopart','/home/re/sql-data-farmer/Harvester/lex_parse.py',339),
  ('dtypeTwopart -> DTYPE_BOTH_1PARAM DTYPE_PART2 LPAREN parameter RPAREN','dtypeTwopart',5,'p_dtypeTwopart','/home/re/sql-data-farmer/Harvester/lex_parse.py',340),
  ('dtypeTimezone -> DTYPE_TIMEZONE_PARAM LPAREN parameter RPAREN','dtypeTimezone',4,'p_dtypeTimezone','/home/re/sql-data-farmer/Harvester/lex_parse.py',359),
  ('dtypeTimezone -> DTYPE_TIMEZONE_PARAM IDENTIFIER DTYPE_TIMEZONE_PARAM IDENTIFIER','dtypeTimezone',4,'p_dtypeTimezone','/home/re/sql-data-farmer/Harvester/lex_parse.py',360),
  ('dtypeTimezone -> DTYPE_TIMEZONE_PARAM LPAREN parameter RPAREN IDENTIFIER DTYPE_TIMEZONE_PARAM IDENTIFIER','dtypeTimezone',7,'p_dtypeTimezone','/home/re/sql-data-farmer/Harvester/lex_parse.py',361),
  ('moreDimensions -> moreDimensions oneDimension','moreDimensions',2,'p_moreDimensions','/home/re/sql-data-farmer/Harvester/lex_parse.py',398),
  ('moreDimensions -> empty','moreDimensions',1,'p_moreDimensions','/home/re/sql-data-farmer/Harvester/lex_parse.py',399),
  ('oneDimension -> LBRACKET RBRACKET','oneDimension',2,'p_oneDimension','/home/re/sql-data-farmer/Harvester/lex_parse.py',402),
  ('oneDimension -> LBRACKET NUMBER RBRACKET','oneDimension',3,'p_oneDimension','/home/re/sql-data-farmer/Harvester/lex_parse.py',403),
  ('constraintPart -> constraintPart constraints','constraintPart',2,'p_constraintPart','/home/re/sql-data-farmer/Harvester/lex_parse.py',427),
  ('constraintPart -> empty','constraintPart',1,'p_constraintPart','/home/re/sql-data-farmer/Harvester/lex_parse.py',428),
  ('constraints -> NOT NULL','constraints',2,'p_constraints','/home/re/sql-data-farmer/Harvester/lex_parse.py',433),
  ('constraints -> NULL','constraints',1,'p_constraints','/home/re/sql-data-farmer/Harvester/lex_parse.py',434),
  ('constraints -> UNIQUE','constraints',1,'p_constraints','/home/re/sql-data-farmer/Harvester/lex_parse.py',435),
  ('parameter -> NUMBER','parameter',1,'p_parameter','/home/re/sql-data-farmer/Harvester/lex_parse.py',451),
  ('moreSequenceBlocks -> moreSequenceBlocks sequenceBlock','moreSequenceBlocks',2,'p_moreSequenceBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',459),
  ('moreSequenceBlocks -> empty','moreSequenceBlocks',1,'p_moreSequenceBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',460),
  ('sequenceBlock -> SEQUENCE IDENTIFIER OWNED BY IDENTIFIER PERIOD IDENTIFIER SEMICOLON','sequenceBlock',8,'p_sequenceBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',468),
  ('moreAlterBlocks -> moreAlterBlocks alterBlock','moreAlterBlocks',2,'p_moreAlterBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',506),
  ('moreAlterBlocks -> empty','moreAlterBlocks',1,'p_moreAlterBlocks','/home/re/sql-data-farmer/Harvester/lex_parse.py',507),
  ('alterBlock -> alterHeader alterBody SEMICOLON','alterBlock',3,'p_alterBlock','/home/re/sql-data-farmer/Harvester/lex_parse.py',512),
  ('alterHeader -> ALTER TABLE ONLY IDENTIFIER','alterHeader',4,'p_alterHeader','/home/re/sql-data-farmer/Harvester/lex_parse.py',518),
  ('alterBody -> ADD CONSTRAINT IDENTIFIER PRIMARY KEY LPAREN IDENTIFIER RPAREN','alterBody',8,'p_alterBody','/home/re/sql-data-farmer/Harvester/lex_parse.py',529),
  ('alterBody -> ADD CONSTRAINT IDENTIFIER FOREIGN KEY LPAREN IDENTIFIER RPAREN REFERENCES IDENTIFIER LPAREN IDENTIFIER RPAREN','alterBody',13,'p_alterBody','/home/re/sql-data-farmer/Harvester/lex_parse.py',530),
  ('alterBody -> multi_attr_constr','alterBody',1,'p_alterBody','/home/re/sql-data-farmer/Harvester/lex_parse.py',531),
  ('multi_attr_constr -> ADD CONSTRAINT IDENTIFIER UNIQUE LPAREN multi_params RPAREN','multi_attr_constr',7,'p_multi_attr_constr','/home/re/sql-data-farmer/Harvester/lex_parse.py',590),
  ('multi_params -> multi_params multi_1param','multi_params',2,'p_multi_params','/home/re/sql-data-farmer/Harvester/lex_parse.py',595),
  ('multi_params -> empty','multi_params',1,'p_multi_params','/home/re/sql-data-farmer/Harvester/lex_parse.py',596),
  ('multi_1param -> IDENTIFIER COMMA','multi_1param',2,'p_multi_1param','/home/re/sql-data-farmer/Harvester/lex_parse.py',601),
  ('multi_1param -> IDENTIFIER','multi_1param',1,'p_multi_1param','/home/re/sql-data-farmer/Harvester/lex_parse.py',602),
  ('empty -> <empty>','empty',0,'p_empty','/home/re/sql-data-farmer/Harvester/lex_parse.py',634),
]
