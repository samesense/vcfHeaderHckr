# vcfHeaderHckr
Force vcf header INFO to have user specified number and type

Are you a fan of vcfanno and gemini, but can't get gemini to include your INFO columns b/c the header INFO Number and Type are screwed up? This is the solution. Replace unlimited INFO Numbers and Types using vcfHeaddrHckr.py.

If you want to replace
* INFO AA_AC's Number with Number_AAA, and its Type with Type_BB 
* and INFO CDP's Number with XX, and its Type with YYY
simple type:

```
python vcfHeadrHckr.py vcfIn vcfOut AA_AC,Number_AAA,Type_BB CDP,XX,YYY
```

Now you're ready for gemini.
