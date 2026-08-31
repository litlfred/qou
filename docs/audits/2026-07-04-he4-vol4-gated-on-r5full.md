# ⁴He Vol₄ is gated on R5-full (the categorical SDP), not on missing infrastructure

**Status:** FINDING (corpus-grounded synthesis, no new compute). The A=4 attempt
to verify the bond-count back-out `Vol₄ ≈ 8.046` by *identifying* ⁴He's binding
link resolves not to a computation I can run, but to an already-open corpus gate:
the single-hyperbolic-link premise is under structural suspicion at the A≤3
anchors themselves. This closes the A=4 link investigation opened in
[#3298](https://github.com/litlfred/qou/pull/3298).

## What the A=4 attempt established

Follows the #3298 finding (naive braid closure ≠ the binding links) and the
correction in this PR (general-n Hoefsmit exists; no Clarabel). Chasing the
Jones-polynomial identification route surfaced four facts, in order:

1. **The canonical atomic word is an intrinsic Hecke superposition.** The
   operator-valued `atom_braid_word_3A(Z,N)` has `k` "averaged" inter-nucleon
   interfaces `σ_g − (h/2)·1`, each a 2-term superposition, so `T_w` is a
   superposition of `2^k` pure braids — verified: ³H/³He `k=7` (128 terms),
   **⁴He `k=9` (512 terms)**. There is no single braid to close (confirming
   #3298 structurally).

2. **The Markov trace collapses the superposition to one Jones polynomial.** The
   corpus already implements the principled identification —
   [`atom_nf_symbolic_D.py`](../../computations/atom_nf_symbolic_D.py): build the
   atom Hecke element via Gröbner–Shirshov normal form, take its Markov trace
   `= J(q)` (well-defined for the Hecke element regardless of the superposition),
   and match to a census knot. `build_atom_nf_symbolic(Z,N)` is general in
   `(Z,N)`, so the method *is* extensible to ⁴He.

3. **But the method does not confirm the binding-link IDs even at A=2.** For ²H,
   the 3A-strand atom braid gives `tr_M(q₀) ≈ 0.388` (convention C; the
   canonical convention-D value is `0.5751722439177719` — but see the note
   below: **neither value belongs in this comparison**, and the gate's real
   evidence is the ratio test, which it passes as a refutation)
   ([`atom-nf-symbolic-D.witness.json`](../../computations/atom-nf-symbolic-D.witness.json)),
   while `J_{6_2}(q₀) ≈ 1.027`. They do not match. Per
   [`2h-markov-trace-zero-audit.md`](2h-markov-trace-zero-audit.md), the trace
   function itself is verified correct (canonical `tr_M` identities pass), so the
   mismatch is structural, not a bug.

> **🛑 The raw-value comparison in this section is NOT the evidence for the
> gate — corrected 2026-08-31, twice.** The producer cited here,
> `atom_nf_symbolic_D.py`, converts its Markov trace to a Jones polynomial via
> `markov_trace_to_jones`, which **is the identity function**: its own
> docstring names the normalisation factor
> `((-1/√q)^{n-1} · (q/(1−q²))^{n-1})` and then says *"for ease, we return
> `tr` as-is"*. So `tr_M(²H) ≈ 0.388` is an **unnormalised** 6-strand Markov
> trace and `J_{6₂}(q₀) ≈ 1.027` is a **normalised** Jones polynomial. They are
> expected to differ, and the size of the gap carries no information about the
> identification. **Do not quote the pair, or any percentage derived from it.**
>
> **The gate is nevertheless SOUND, on evidence this section does not cite.**
> The producer knows the normalisation is missing and computes the
> convention-independent discriminator instead — *"even if they differ by a
> writhe/normalization factor, the ratio should be a pure power of
> `−q^{1/2}`"* — recorded as `symbolic_ratio` in the witness. Measured: a
> rational function with **83 terms over 11**, in half-integer powers running
> past `q^{2713/2}`. **Not a monomial, so the ratio test fails and the anchor
> non-confirmation is real.**
>
> An earlier version of this note scoped `0.388` as convention-C against the
> canonical convention-D `0.5751722439177719` and reported the gap as
> "62.19 % / 43.99 % low". **That scoping is correct about the `tr_M` value and
> irrelevant here:** correcting an input to a comparison that was never
> evidential does not make it evidential. A future attempt on
> `conj:canonical-knot-id-sdp` should aim at the **ratio**, not the gap.
> Measured by `computations/probes/r5full_anchor_gate_evidence_probe.py` (3/3).

4. **The A≤3 IDs are deprecated volume-search matches.** `2h-markov-trace-zero-audit.md`
   records that 6_2 (²H), 8_11 (³H), and L6a4 (³He) were assigned by *volume
   search* — `Vol_hyp(K) ≈ B_AME/m_e` — carrying `manual-historical-volume-match`
   tags and corroborating PSD-cone anomalies (α\* = 0.546 for ²H, 0.424 for ³H),
   flagged `deprecated-volume-match`. They were never derived from the categorical
   pipeline.

## The gate

The ⁴He 4-body link — and hence `Vol₄` — is therefore gated on **R5-full**: the
categorical SDP that "produces canonical `T_w` from the categorical pipeline
directly" (the open canonical-knot-ID, `conj:canonical-knot-id-sdp`, #604). Per
the ²H audit, R5-full "may show the atom braid is not the closure of any single
hyperbolic knot" — split/composite links, or trace cancellations, are live
possibilities. Until it lands, there is **no derived single ⁴He binding link**
whose SnapPy volume is `Vol₄`.

## Consequence for the bond-count back-out

`Vol₄ ≈ 8.046` (`theta_mn_bondcount_linearchain.py`, from
`residual = m_e·3·Vol₄`) is a back-out against a framework whose A≤3 anchors are
deprecated volume-search matches that the principled trace test does not confirm.
It cannot be "verified" by identifying a single ⁴He link, because the single-link
premise itself is the open question. The provisional doubly-magic
`2·Vol(Borromean) = 14.655` sits under the same suspicion.

**Scope discipline.** This is scope-(a): the *single-link identification route* is
not established (its A≤3 anchors are deprecated and trace-unconfirmed) — **not** a
refutation of the bond-count model, whose ³H/³He/deuteron binding predictions
stand on their own footing, and **not** a structural exclusion of `Vol₄ ≈ 8.046`.
The value is simply unverifiable until R5-full derives (or refutes) a canonical
⁴He link. Matching a link to 8.046 would be a CAL-4 fit — out of bounds.

## Why no H_12 compute was run

The Jones-ID would compute `J_{T_w(⁴He)}(q)` at H_12 and match a census knot. But
the corpus already shows the method fails to confirm its A≤3 anchors, so an H_12
match (or non-match) would not verify `Vol₄` either way — the framework it lives
in is the thing in question. Running the heavy symbolic H_12 reduction would not
change the verdict. The productive path is R5-full, not this identification.
