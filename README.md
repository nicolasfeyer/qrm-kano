# Google Form to KANO synthesis

Generate a KANO synthesis from Google Form answers.
Questions should be asked in the following order: 
- functional for functionality 1
- dysfunctional for functionality 1
- functional for functionality 2
- dysfunctional for functionality 2
- ...

## How to proceed

1. Export Google Form answers in a TSV file named *answers.tsv*
2. Edit the *answer_options.json* file and add the answer options for your Google form.
3. Edit the *functionalities.txt* file and add the functionalities in the same order as the questions.
4. Run *kano.py* script

## Output example
| Sujet                  | A  | P | O | I  | C  | D |
|------------------------|----|---|---|----|----|---|
| Réveil vibration       | 10 | 0 | 0 | 9  | 15 | 0 |
| Réveil audio           | 17 | 3 | 0 | 11 | 3  | 0 |
| Analyse du sommeil     | 19 | 1 | 0 | 11 | 3  | 0 |
| Massage                | 19 | 2 | 0 | 9  | 4  | 0 |
| Domotique              | 10 | 3 | 0 | 14 | 7  | 0 |
| Mode ne pas déranger   | 6  | 2 | 0 | 17 | 9  | 0 |
| Mode chauffage         | 14 | 2 | 0 | 6  | 12 | 0 |
| Mode froid             | 18 | 1 | 0 | 9  | 6  | 0 |
| Réglages inclinaison   | 17 | 3 | 1 | 13 | 0  | 0 |
| Plateau repas          | 10 | 0 | 0 | 13 | 11 | 0 |
| Facilement compactable | 19 | 0 | 0 | 14 | 1  | 0 |
