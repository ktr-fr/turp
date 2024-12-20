# turp

## Projet d'acculturation en Sciences de la Donnée pour les vieux briscards sous CBL vers les jeunes léopards du FULLWEB

### Premier jet sur la notion similarité/dissimilarité

#### Distances Euclidoienne, de Manhattan, et de Chebychev


```COBOL
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DISTANCE-CALC.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       REPOSITORY.
           FUNCTION ALL INTRINSIC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-X1 PIC S9(5)V99.
       01 WS-Y1 PIC S9(5)V99.
       01 WS-X2 PIC S9(5)V99.
       01 WS-Y2 PIC S9(5)V99.
       01 WS-EUCLIDEAN PIC 9(5)V99.
       01 WS-MANHATTAN PIC 9(5)V99.
       01 WS-CHEBYSHEV PIC 9(5)V99.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           MOVE 0 TO WS-X1 WS-Y1 WS-X2 WS-Y2
           ACCEPT WS-X1
           ACCEPT WS-Y1
           ACCEPT WS-X2
           ACCEPT WS-Y2

           COMPUTE WS-EUCLIDEAN = 
               SQRT((WS-X2 - WS-X1) ** 2 + (WS-Y2 - WS-Y1) ** 2)

           COMPUTE WS-MANHATTAN = 
               ABS(WS-X2 - WS-X1) + ABS(WS-Y2 - WS-Y1)

           COMPUTE WS-CHEBYSHEV = 
               FUNCTION MAX(ABS(WS-X2 - WS-X1), ABS(WS-Y2 - WS-Y1))

           DISPLAY WS-EUCLIDEAN
           DISPLAY WS-MANHATTAN
           DISPLAY WS-CHEBYSHEV

           STOP RUN.

```
           
