# =======================================================================
# FILE:        Makefile
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains useful commands for this project. You
#              may use the following commands:
#
#              - make            - compiles the project and places
#                                  the executable in the bin folder
#
#              - make submission - creates the the submission, you will
#                                  submit.
#
#              - Don't make changes to this file unless you took CS 143A.
# =======================================================================

RAW_SOURCES = \
	Main.py\
	BTSolver.py\
	Constraint.py\
	ConstraintNetwork.py\
	Domain.py\
	SudokuBoard.py\
	Trail.py\
	Variable.py

SOURCE_DIR = src
BIN_DIR = bin
SOURCES = $(foreach s, $(RAW_SOURCES), $(SOURCE_DIR)/$(s))

all: $(SOURCES)
	@python3 -m compileall -qb src
	@rm -rf $(BIN_DIR)
	@mkdir -p $(BIN_DIR)
	@mv -f src/*.pyc bin

submission: all
	@rm -f *.zip
	@python3 make-report.py
	@zip -9rqq s_sugokuAI.zip $(SOURCE_DIR) $(BIN_DIR)

run:
	@python3 src/Main.py MRV LCV FC
