## Cross-paper + uploads + wiring scans

- **`unital-groebner-bases/`** — no overlap with BlochGroup,
  Cl_2, archimedean-functor, or crystal-basis content.
- **`fred2005-formal-groups/`** — contains
  [`unit-root-F-crystal`](../../fred2005-formal-groups/formal-groups-chapter/unit-root-f-crystal.md)
  and `unit-root-iff-integrable`. *Different* notion of "crystal"
  (Berthelot-Ogus F-crystal in formal-groups context, distinct
  from Kashiwara crystal). Cross-paper integration possible at
  the level of *both being categorical / motivic objects*, but
  the math is structurally distinct — no immediate filler-sharing
  opportunity.
- **`uploads/`** — 14 PDFs present (`0008040v1.pdf`,
  `0911.4494v2.pdf`, etc.). Text-grep on the binary PDFs returned
  no hits for `Bloch | Clausen | dilog | figure-8`, so either the
  PDFs lack OCR-extracted text or the keywords are absent. A
  proper intake via `local/document-intake` skill would surface
  any relevant content; out of scope for this filler push.
- **Wiring follow-up:** `crt_markov.py` currently has no
  `solve_y_lambda` reference — the user is preparing the
  modification. Recommendation per the prior turn stands: add
  `solve_y_lambda_numerical(n, q_value)` as a *separate* function
  in `markov_weights_symbolic.py`, leave the symbolic version
  intact for `y_lambda_equivalence_proof.py:60` to consume.
