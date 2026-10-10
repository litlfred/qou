# Orphan witnesses

`option-e-deuteron-delta-lambda-probe.witness.json` sat at
`computations/probes/` on main, but nothing writes that path. Its producer,
`computations/probes/option_e_deuteron_delta_lambda_probe.py`, writes
`computations/option-e-deuteron-delta-lambda-probe.witness.json`, which is the
live copy. This copy has been frozen since 2026-07-19 at the convention-C deuteron
value (`B_pred_over_me = -0.38828642…`), while the live value is
`-0.15196833…`. It was moved here on 2026-10-10 on the owner's instruction
(bean qou-bvk7), so it is kept as a record and not read as current.
