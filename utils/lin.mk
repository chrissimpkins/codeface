# Generates images/*-lin.png files using Pango, Cairo, and FreeType for
# rendering on Linux.  The named font files must be installed on the system
# (easiest is to copy the fonts directory to ~/.fonts and run fc-cache -fv)
# and the rendering will obey the current hinting settings.
#
# To run, cd into the images directory and type 'make -f ../util/lin.mk'

.PHONY: all
all: anonymous-pro-lin.png aurulent-sans-mono-lin.png						\
     bitstreamverasansmono-lin.png bp-mono-lin.png code-new-roman-lin.png	\
     coding-font-tobi-noaa-lin.png consola-mono-lin.png cousine-lin.png		\
     crisp-lin.png cutive-mono-lin.png dejavu-sans-mono-lin.png				\
     dina-lin.png droid-sans-mono-lin.png edlo-lin.png						\
     elronet-monospace-lin.png fantasque-sans-mono-lin.png					\
     fira-mono-lin.png fixed-sys-excelsior-lin.png free-mono-lin.png		\
     inconsolata-dz-lin.png inconsolata-g-lin.png inconsolata-lgc-lin.png	\
     inconsolata-lin.png lekton-lin.png liberation-mono-lin.png				\
     luculent-lin.png luxi-mono-lin.png meslo-lin.png metrickal-lin.png		\
     mono-mmm-5-lin.png mono-one-lin.png mono-spatial-lin.png				\
     monofur-lin.png monoid-lin.png monospace-typewriter-lin.png			\
     monospace-lin.png mplus1m-lin.png mplus2m-lin.png						\
     not-courier-sans-lin.png office-code-pro-lin.png oxygen-mono-lin.png	\
     panic-sans-mono-lin.png pixel-carnage-noaa-lin.png						\
     pro-font-windows-lin.png proggy-clean-noaa-lin.png						\
     proggy-small-noaa-lin.png proggy-square-noaa-lin.png					\
     proggy-tiny-noaa-lin.png pt-mono-lin.png roboto-mono-lin.png			\
     sax-mono-lin.png share-tech-mono-lin.png small-type-writing-lin.png	\
     source-code-pro-lin.png sv-basic-manual-lin.png terminus-lin.png		\
     tex-gyre-cursor-lin.png ubuntu-mono-lin.png verily-serif-mono-lin.png

deps = ../utils/render.py ../samplecode/compact.c
action = python ../utils/render.py -t ../samplecode/compact.c -l c -x 725 -b "\#ddddddff" -i $@ -f
anonymous-pro-lin.png: $(deps)
	$(action) "Anonymous Pro 16"
aurulent-sans-mono-lin.png: $(deps)
	$(action) "Aurulent Sans Mono 16" -r
bitstreamverasansmono-lin.png: $(deps)
	$(action) "Bitstream Vera Sans Mono 16" -r
bp-mono-lin.png: $(deps)
	$(action) "BPmono 16" -r
code-new-roman-lin.png: $(deps)
	$(action) "Code New Roman, 16"
coding-font-tobi-noaa-lin.png: $(deps)
	$(action) "CodingFontTobi 16" -r -m bilevel
consola-mono-lin.png: $(deps)
	$(action) "Consola Mono 16" -r
cousine-lin.png: $(deps)
	$(action) "Cousine 16"
crisp-lin.png: $(deps)
	$(action) "Crisp 16" -r
cutive-mono-lin.png: $(deps)
	$(action) "Cutive Mono 16" -r
dejavu-sans-mono-lin.png: $(deps)
	$(action) "DejaVu Sans Mono 16"
dina-lin.png: $(deps)
	$(action) "Dina ttf 10px 16" -r
droid-sans-mono-lin.png: $(deps)
	$(action) "Droid Sans Mono 16" -r
edlo-lin.png: $(deps)
	$(action) "Edlo 16" -r
elronet-monospace-lin.png: $(deps)
	$(action) "ElroNet Monospace 16" -r
fantasque-sans-mono-lin.png: $(deps)
	$(action) "Fantasque Sans Mono 16"
fira-mono-lin.png: $(deps)
	$(action) "Fira Mono 16" -r
fixed-sys-excelsior-lin.png: $(deps)
	$(action) "Fixedsys Excelsior 3.01 16" -r
free-mono-lin.png: $(deps)
	$(action) "FreeMono 16"
inconsolata-dz-lin.png: $(deps)
	$(action) "Inconsolata-dz 16" -r
inconsolata-g-lin.png: $(deps)
	$(action) "Inconsolata-g 16" -r
inconsolata-lgc-lin.png: $(deps)
	$(action) "Inconsolata LGC 16" -r
inconsolata-lin.png: $(deps)
	$(action) "Inconsolata 16"
lekton-lin.png: $(deps)
	$(action) "Lekton 16" -r
liberation-mono-lin.png: $(deps)
	$(action) "Liberation Mono 16"
luculent-lin.png: $(deps)
	$(action) "Luculent 16"
luxi-mono-lin.png: $(deps)
	$(action) "Luxi Mono 16"
meslo-lin.png: $(deps)
	$(action) "Meslo LG M DZ 16" -r
metrickal-lin.png: $(deps)
	$(action) "Metrickal 16" -r
mono-mmm-5-lin.png: $(deps)
	$(action) "monoMMM_5 16" -r
mono-one-lin.png: $(deps)
	$(action) "monoOne 16" -r
mono-spatial-lin.png: $(deps)
	$(action) "MonoSpatial 16" -r
monofur-lin.png: $(deps)
	$(action) "monofur 16" -r
monoid-lin.png: $(deps)
	$(action) "Monoid 16" -r
monospace-typewriter-lin.png: $(deps)
	$(action) "MonospaceTypewriter 16" -r
monospace-lin.png: $(deps)
	$(action) "Monospace 16" -r
mplus1m-lin.png: $(deps)
	$(action) "M+ 1m 16" -r
mplus2m-lin.png: $(deps)
	$(action) "M+ 2m 16" -r
not-courier-sans-lin.png: $(deps)
	$(action) "NotCourierSans 16" -r
office-code-pro-lin.png: $(deps)
	$(action) "Office Code Pro 16"
oxygen-mono-lin.png: $(deps)
	$(action) "Oxygen Mono 16" -r
panic-sans-mono-lin.png: $(deps)
	$(action) "Panic Sans 16"
pixel-carnage-noaa-lin.png: $(deps)
	$(action) "PixelCarnageMonoTT 16" -r -m bilevel
pro-font-windows-lin.png: $(deps)
	$(action) "ProFontWindows 16" -r
proggy-clean-noaa-lin.png: $(deps)
	$(action) "ProggyCleanTT 16" -r -m bilevel
proggy-small-noaa-lin.png: $(deps)
	$(action) "ProggySmallTT 16" -r -m bilevel
proggy-square-noaa-lin.png: $(deps)
	$(action) "ProggySquareTT 16" -r -m bilevel
proggy-tiny-noaa-lin.png: $(deps)
	$(action) "ProggyTinyTT 16" -r -m bilevel
pt-mono-lin.png: $(deps)
	$(action) "PT Mono 16"
roboto-mono-lin.png: $(deps)
	$(action) "Roboto Mono 16"
sax-mono-lin.png: $(deps)
	$(action) "saxMono 16" -r
share-tech-mono-lin.png: $(deps)
	$(action) "Share-TechMonoTrue 16" -r
small-type-writing-lin.png: $(deps)
	$(action) "SmallTypeWriting 16" -r
source-code-pro-lin.png: $(deps)
	$(action) "Source Code Pro 16"
sv-basic-manual-lin.png: $(deps)
	$(action) "SV Basic Manual 16" -r
terminus-lin.png: $(deps)
	$(action) "Terminus 16" -r
tex-gyre-cursor-lin.png: $(deps)
	$(action) "TeX Gyre Cursor 16" -r
ubuntu-mono-lin.png: $(deps)
	$(action) "Ubuntu Mono 16"
verily-serif-mono-lin.png: $(deps)
	$(action) "Verily Serif Mono 16" -r
