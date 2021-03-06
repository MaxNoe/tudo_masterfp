all: build/main.pdf

mplfiles = ../matplotlibrc ../header-matplotlib.tex

pyoptions = MATPLOTLIBRC=$(shell pwd)/../ TEXINPUTS=$(shell pwd)/..:

build/impuls.pdf: scripts/plot_impuls.py
	$(pyoptions) python scripts/plot_impuls.py


build/attenuation_fft.pdf build/attenuation_signal.pdf: data/att_long_102_9kHz_fft.csv data/att_short_102_9kHz_fft.csv scripts/attenuation_factor.py $(mplfiles)
	$(pyoptions) python scripts/attenuation_factor.py

build/lcrg.pdf: build/length.yaml data/rg058-85m-lcrg.csv scripts/plot_lcrg.py | build
	$(pyoptions) python scripts/plot_lcrg.py

build/length_measurement.pdf: data/reflek1.csv scripts/plot_length_measurement.py | build
	$(pyoptions) python scripts/plot_length_measurement.py

build/unknown.pdf: scripts/plot_unknown.py | build
	$(pyoptions) python scripts/plot_unknown.py

build/time_constant_fit.pdf build/k2a2_c.tex build/k2a2_r.tex build/k1a6_l.tex build/k1a6_r.tex: scripts/plot_time_constant_fit.py | build
	$(pyoptions) python scripts/plot_time_constant_fit.py

build/multiple_reflection.pdf: scripts/plot_multiple_reflection.py | build
	$(pyoptions) python scripts/plot_multiple_reflection.py

build/length.yaml build/length.tex: scripts/calc_length.py | build
	python scripts/calc_length.py







plots = $(addprefix build/, $(addsuffix .pdf, \
	attenuation_signal \
	attenuation_fft \
	lcrg \
	length_measurement \
	unknown \
	multiple_reflection \
	impuls \
	time_constant_fit \
	))


build/main.pdf: FORCE $(plots) build/length.tex build/k2a2_c.tex build/k2a2_r.tex build/k1a6_l.tex build/k1a6_r.tex| build
	TEXINPUTS=build:..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

preview: FORCE $(plots) build/length.tex build/k2a2_c.tex build/k2a2_r.tex build/k1a6_l.tex build/k1a6_r.tex| build
	TEXINPUTS=build:..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  -pvc \
	main.tex


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
