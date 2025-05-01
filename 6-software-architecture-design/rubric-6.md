# Rubric for Assignment 6

## Submission (12 points)

The submission should consist of three (optionally four) files:

- `tic_tac_toe_view.py`
- `tic_tac_toe_controller.py`
- `tic_tac_toe_game.py`
- `llm.md` (Optional)

### Effort (9 points)

For each file:

3: Changes to the file seem to show a good-faith attempt on all problem parts
relating to this file.

2: Changes to the file seem to show a good-faith attempt on at least 50% (but
strictly less than 100%) of problem parts relating to this file.

1: Changes to the file seem to show a good-faith attempt on less than 50% (but
strictly more than 0%) of problem parts relating to this file.

0: The file was unchanged from its initial state.

In this section, taking one or more late days results in full credit.

**Points: 9/9**

#### Grader Comments

*None.*

### Scope of Changes (3 points)

3: No files are added, changed, or deleted other than those listed above.

2: One file was added, changed, or deleted other than those listed above.

1: Two files were added, changed, or deleted other than those listed above.

0: Three or more files were added, changed, or deleted other than those listed
above.

**Points: 3/3**

#### Grader Comments

*None.*

### Submission Summary

**Points: 12/12**

## Correctness (36 points)

The rubric describes some but not all possible point values and the criteria
that correspond to these values. Other point values are possible and given
subject to grader discretion.

### 1. An Inherited View (and an Acquired Taste) (14 points)

The code for this problem is in `tic_tac_toe_view.py`.

#### 1.1. As Easy as `abc` (7 points)

This part covers the classes `TicTacToeView` and `TextView` (implicitly) in
`tic_tac_toe_view.py`.

7: The implementation passes all unit tests.

4: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: 7/7**

##### Grader Comments

*None.*

#### 1.2. A More Concrete View (7 points)

This part covers the `draw` method of the `TextView` class in
`tic_tac_toe_view.py`.

7: The implementation passes all unit tests.

4: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: 7/7**

##### Grader Comments

*None.*

#### 1. An Inherited View (and an Acquired Taste) Summary

**Points: 14/14**

### 2. Taking Control (14 points)

The code for this problem is in `tic_tac_toe_controller.py`.

#### 2.1. Class Structure (7 points)

This part covers the classes `TicTacToeController` and `TextController`
(implicitly) in `tic_tac_toe_controller.py`.

7: The implementation passes all unit tests.

4: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: 7/7**

##### Grader Comments

*None.*

#### 2.2. Move Input Processing (7 points)

This part covers the `move` method of the `TextController` class in
`tic_tac_toe_controller.py`.

7: The implementation passes all unit tests.

4: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: 7/7**

##### Grader Comments

*None.*

#### 2. Taking Control Summary

**Points: 14/14**

### 3. All Together Now (8 points)

The code for this problem is in `tic_tac_toe_game.py`, and concerns the `main`
function.

8: The implementation passes all unit tests.

5: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: 8/8**

#### Grader Comments

*None.*

### Correctness Summary

**Points: 36/36**

## Style (52 points)

### General (2 points)

2: The submission contains at most one spelling/grammar mistake.

1: The submission contains a few spelling/grammar mistakes.

0: The submission contains a substantial number of spelling/grammar mistakes.

**Points: 2/2**

#### Grader Comments

*None.*

### Git (5 points)

One point for meeting each of the following criteria (checked over all commits
relevant to the submission):

- The header line of commit message succinctly summarizes what was changed.
- The commit message provides context for the changes made.
- The commit does not add, edit, or remove files that are not necessary for
  submission (e.g., adding notes for yourself, or editing/removing the Jupyter
  notebook describing the assignment).
- The commit does not contain Git conflict indicators (e.g., `<<<<<<< HEAD`)
  that need to be removed during grading.
- The commit message does not contain lines that exceed 72 characters in length.

**Points: 5/5**

#### Grader Comments

*None.*

### Python (45 points)

#### Black (3 points)

For each of the 3 files submitted:

1: Black reports no formatting changes it would make to the file.

0: Black reports a formatting change it would make to the file.

**Points: 2/3**

##### Grader Comments

*None.*

#### Pylint (10 points)

Pylint, when run, returns a "style score" out of 10. After running this on all
Python files, take the style score and round it _down_, with minimum of 0
points.

**Points: 9/10**

##### Grader Comments

*None.*

#### Docstrings (26 points)

This section covers docstrings for the functions listed below. For each
function:

2: The docstring is present, well-written, and includes all required
information.

1: The docstring has a minor error, such as not mentioning or explaining a
parameter/return type. (The parameter/return type is not required if there is
none, or if all information is easily and explicitly in the docstring summary.)

0: The docstring is missing or unchanged from the starter code.

* `tic_tac_toe_view.py`: `TicTacToeView`: **2/2**
* `tic_tac_toe_view.py`: `__init__`: **2/2**
* `tic_tac_toe_view.py`: `board`: **2/2**
* `tic_tac_toe_view.py`: `TicTacToeView.draw`: **2/2**
* `tic_tac_toe_view.py`: `TextView`: **2/2**
* `tic_tac_toe_view.py`: `TextView.draw`: **2/2**
* `tic_tac_toe_controller.py`: `TicTacToeController`: **2/2**
* `tic_tac_toe_controller.py`: `__init__`: **2/2**
* `tic_tac_toe_controller.py`: `board`: **2/2**
* `tic_tac_toe_controller.py`: `TicTacToeController.move`: **2/2**
* `tic_tac_toe_controller.py`: `TextController`: **2/2**
* `tic_tac_toe_controller.py`: `TextController.move`: **2/2**
* `tic_tac_toe_game.py`: `main`: **2/2**

**Points: 26/26**

##### Grader Comments

*None.*

#### Miscellaneous Code Style (6 points)

Outside of where they are already covered by other parts of this rubric,
consider the following criteria (1 point each):

- Variable names follow the course guidelines for formatting and
  descriptiveness.
- The code consistently uses single or double quotes except where it would be
  convoluted to write.
- The code uses Python features taught in class (e.g., f-strings instead of
  `print` with multiple arguments, `str.format()`, or `%`-style strings).
- The code avoids "unpythonic" ways of writing things (e.g., `if x == True`
  instead of `if x`).
- Where needed, there are comments in the code to describe what a block of code
  does (at a high level) or why that code is there.
- The code is generally readable and easy to understand.

**Points: 6/6**

##### Grader Comments

*None.*

#### Python Summary

**Points: 43/45**

### Style Summary

**Points: 50/52**

## Summary

**Submission: 12/12**

**Correctness: 36/36**

**Style: 50/52**

### Total

**TOTAL POINTS: 98/100**

### General Grader Comments

*None.*

### Grader Information

*Grader*: Miles Mezaki <mmezaki@olin.edu>

*Reviewer*: Maya Cranor <mcranor@olin.edu>

