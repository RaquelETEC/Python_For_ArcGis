import arcpy
arcpy.ImportToolbox(r"")
arcpy.Desafio0001atbx.Model()

arcpy.management.SelectLayerByAttribute(r"Biomas\BRA_BIOMAS", "NEW_SELECTION", "NOME = 'Amazônia'", None)