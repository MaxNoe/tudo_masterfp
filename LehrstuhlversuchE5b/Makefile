texoptions = -lualatex \
			 -output-directory=build \
			 -interaction=nonstopmode \
			 -halt-on-error

performances = $(addprefix build/, NaiveBayes.hdf5 RandomForest.hdf5 AdaBoost.hdf5)

all: build/poster.pdf


build/poster.pdf: FORCE build/rocs_performance.pdf  build/rocs_performance_feature_selection.pdf  build/precision_recall.pdf build/roc_table.tex build/roc_table_feature_selection.tex| build
	BIBINPUTS=.. TEXINPUTS=images:build: latexmk $(texoptions) poster.tex

build/rocs_performance.pdf: plot_rocs.py matplotlibrc $(performances) | build
	TEXINPUTS=$(shell pwd): python plot_rocs.py 'performance'
	TEXINPUTS=$(shell pwd): python plot_rocs.py 'performance_feature_selection'

build/precision_recall.pdf: plot_precision_recall.py matplotlibrc $(performances) | build
	TEXINPUTS=$(shell pwd): python plot_precision_recall.py

build/roc_table.tex: calc_rocs.py $(performances) | build
	python calc_rocs.py

$(performances): cross_validation.py | build
	python cross_validation.py

FORCE:

build:
	mkdir -p build

clean:
	rm -rf build
