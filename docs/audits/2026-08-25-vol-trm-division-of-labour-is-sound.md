# The `Vol` / `tr_M` division of labour is sound; the bridge between them is not

**2026-08-25 · bean `qou-qpj9` · scope (a) · no new computation — a reading of
existing code, following up
[the Ito/Dehornoy audit](2026-08-25-ito-dehornoy-hyperbolicity-criterion.md)
Addendum 4.**

## The worry, and why it does not materialise

Addendum 4 established that the atom object is **not a link**: what
`atom_braid_word_3A` returns is an element of `H_n(q)` outside `im(ρ)`, because
`2A+1` of its letters are genuine weight-1 averages over crossing sign. The
obvious follow-on worry is that the mass law reads `Vol(K)`, and if the atom has
no link then something must be reading a volume off an object that has none.

**Nothing is.** Traced through the live consumers:

| quantity | comes from | is it a link? |
|---|---|---|
| `Vol(K)` | the **atlas knot** — `𝓑₃`, `6₂`, `8₁₁`, `L6a4` | **yes**, genuine links |
| `tr_M(K)` / `ρ(K)` | the **atom `H_n(q)` element** | **no — and it needs none** |

The Markov trace is a linear functional on all of `H_n(q)`, so it is defined on
the atom element without any closure. The volume is only ever taken of an atlas
knot. `per_knot_density_per_block_wiring.py` states the per-block form over
*"partitions of the **knot's own** strand count"* and works it for `𝓑₃`; the
production scalar is `[Vol(𝓑₃)/ℏ_q²]·linking_weight(q)`, a constant of the
**Borromean link**, not of any atom word.

The one producer that *does* push the atom word through SnapPy —
[`vol_t_he3_snappy_probe.py`](../../computations/deltalambda/vol_t_he3_snappy_probe.py)
— is exploratory, says so, comments the averaged letters as *"Hecke element
`σ−h/2·1`, not a topological crossing"*, and returns a refutation.

**So the division of labour is already correct throughout.** Recorded as a
negative because it was my own worry and it failed — the second one this arc.

## What is actually missing

The two halves are each sound; **what is unestablished is that they are about the
same object.** The atlas knot stands in for the atom, and the right to make that
substitution is exactly what the previous two addenda found unsupported:

- **The general principle offered was *"Same Markov class"*** — corrected in
  Addendum 6, because a non-braid has no Markov class to share.
- **For `D` / `T` / `³He` the actual selection is a fit** — the knot chosen for
  volume proximity to `B_AME`
  ([sibling audit](2026-08-25-knot-id-is-an-admitted-fit.md)).
- **For `p` / `n` it is sound** — the volume comes from the particle registry's
  canonical `T_w` σ-braid word (Addendum 7), a genuine braid.

That is the gap, stated precisely: **not a dataflow defect, a warrant defect.**
`tr_M` legitimately reads the atom element; `Vol` legitimately reads a link; and
for three of six atlas entries there is no principled reason those two readings
concern the same physical object.

## What this does and does not imply

**Does not** imply any volume or binding number is wrong. Nothing here recomputes
anything.

Worth noting for calibration rather than as a further claim: the surviving
consumers of `per-atom-hyperbolic-volume.witness.json` are absolute-mass tables
(`mass_table_comprehensive.py`, `per_knot_mass_table_demonstration.py`), and
[`canonical_mass.py`](../../computations/canonical_mass.py) already deprecates
exactly these `Vol`-based forms for absolute mass — *"`m_e · Vol(𝓑₃) · tr_M / ℏ_q²`
→ 406 (−57 %)"*. Under the 2026-08-11 excision ruling absolute mass is a
rendering rather than a prediction, so the warrant gap above sits under a claim
the framework has already stepped back from. It still wants closing, because the
same substitution is what a *binding-ratio* reading would rely on, and binding
ratios are not excised.

## Cross-references

- Addendum 4, 6, 7 — [Ito/Dehornoy audit](2026-08-25-ito-dehornoy-hyperbolicity-criterion.md)
- The admitted fit — [sibling audit](2026-08-25-knot-id-is-an-admitted-fit.md)
- Atlas provenance, unenforced — bean `qou-4b6g`
