# KiCad JLCPCB BOM Plugin

Extract a JLCPCB-compliant bill of materials directly from your KiCad schematic.

## Installation
This script requires Python 3.x version.

The script has been tested with KiCad 7.0.0

1. Copy bom_csv_jlcpcb.py to your KiCad installation folder under the "~KiCad/7.0/bin/scripting/plugins" directory
2. In Eschema (the Schematics editor) go to "Tools(도구)" -> "Generate Bill of Materials(BOM생성)", press the "+" button at the bottom of the screen, and choose the plugin file you have just copied. When asked for a nickname, go with the default, "bom_csv_jlcpcb".

## Usage
Instructions for exporting JLCPCB BOM from KiCad's Eschema:

1. Go to "Tools" -> "Generate Bill of Materials"
2. Choose "bom_csv_jlcpcb" from the "BOM plugins" list on the left
3. Make sure the command line starts with "python3" instead of "python" (unless your default python version is 3)
4. Make sure the command line ends with "%O.csv" (otherwise, change "%O" into "%O.csv")
5. Click on "Generate". The BOM file should be created inside your project's directory, as a ProjectName.CSV file.

## Custom Fields
You can customize the script's output by adding the following fields to your components:

"LCSC" - Add this field to include an LCSC Part number in the generated BOM. e.g.: C2286 for a red LED.
"LCSC" - Set this field to 0 (or "False") to omit the component from the generated BOM.
