#
# Example python script to generate a BOM from a KiCad generic netlist
# bom_csv_jlcpcb.py
# BOM plugins Sorted and Grouped CSV BOM
#

"""
    @package
    Generate a JLCPCB-compliant BOM directly from your KiCad schematic.
    Components are sorted by ref and grouped by value with same footprint.
    LCSC Part numbers are copied from the "LCSC" field, if exists.
    It is possible to hide components from the BOM by setting the 
    "LCSC" field to "0" or "false".

    Output fields:
    'Comment', 'Designator', 'Footprint', 'LCSC Part #'

    Command line:
    python "pathToFile/bom_csv_jlcpcb.py" "%I" "%O.csv"
    
    Installation : 
    "Tools(도구)" -> "Generate Bill of Materials(BOM생성)", 
    press the "+" button at the bottom of the screen, 
    and choose the plugin file you have just copied.
    
    Usage :
    Go to "Tools" -> "Generate Bill of Materials"
    Choose "bom_csv_jlcpcb" from the "BOM plugins"
    Click on "Generate". The BOM file should be created inside your project's directory, as a ProjectName.CSV file.
"""

import kicad_netlist_reader
import csv
import sys

net = kicad_netlist_reader.netlist(sys.argv[1])

with open(sys.argv[2], 'w', newline='') as f:
    out = csv.writer(f)
    out.writerow(['Comment', 'Designator', 'Footprint', 'LCSC Part #'])

    for group in net.groupComponents():
        refs = []

        lcsc_pn = ""
        for component in group:
            if component.getField('LCSC') in ['0', 'false', 'False', 'FALSE']:
                continue
            refs.append(component.getRef())
            lcsc_pn = component.getField("LCSC") or lcsc_pn
            c = component

        if len(refs) == 0:
            continue

        # Fill in the component groups common data
        out.writerow([c.getValue(), ",".join(refs), c.getFootprint().split(':')[1], lcsc_pn])
    f.close()