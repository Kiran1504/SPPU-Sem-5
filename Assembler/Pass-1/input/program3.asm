START 101
READ N
MOVER BREG ONE
MOVEM BREG TERM
AGAIN MULT BREG TERM
MOVER CREG TERM
ADD CREG ONE
MOVEM CREG TERM
COMP CREG N
BC LE AGAIN
DIV BREG TWO
MOVEM BREG RESULT
PRINT RESULT
STOP
N DS 1
RESULT DS 1
ONE DC 1
TERM DS 1
TWO DC 2
END
