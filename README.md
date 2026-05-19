# Electronica-Basica
Laboratorio de Electrónica Básica

# Schemdraw

## Instalar 

pip install "schemdraw[svgmath]"

## Configurar
hooks:
  - hooks/schemdraw_hook.py

Creamos carpeta:
    hooks/

## Cstructura ficheros
docs/
└─ procs/
   └─ amp/
      ├─ med-av.md
      └─ images/
         └─ svg/
            └─ med-av-divisor-tension-a1b2c3d4.svg
## Uso 
python scripts\schemdraw\divisor_tension.py
python -m mkdocs serve