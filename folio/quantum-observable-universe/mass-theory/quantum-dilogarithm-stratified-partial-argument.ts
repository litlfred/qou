import { remark } from "../../schema/builders";

export default remark({
  label: "rem:quantum-dilogarithm-stratified-partial-argument",
  interprets: "conj:quantum-dilogarithm-stratified",
  title: "Partial argument for the stratified quantum dilogarithm",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): it is `QOU.BraidKnot.gbDepth`, the supremum of the hook length over the cells of $\\lambda$" },
    {
      kind: "refined-framing",
      body: "**Corrected, and the correction *repairs* Step 4 rather than breaking\nit.** This displayed condition read\n\"whenever $k + \\ell \\neq N$\", followed by *\"the self-dual pairing\n$Z^{(k)} \\times Z^{(N-k)} \\to R$ is the **Poincaré duality of\ncurvature-rank strata**\"* — an **anti-diagonal** duality, imported\nfrom [`prf:spectral-sequence-collapse`](#prf:spectral-sequence-collapse)\n\"§Frobenius duality of strata\", where the same claim has now been\nrefuted in place.\n\nThe strata here are spans of central primitive idempotents, and\ndistinct idempotents **annihilate each other**: for any linear\nfunctional $\\varphi$,\n$\\varphi(e_\\lambda e_\\mu) = \\varphi(\\delta_{\\lambda\\mu} e_\\lambda)$.\nSo the pairing on that basis is $\\mathrm{diag}(\\tau(e_\\lambda))$ —\n**diagonal**, with every stratum self-dual and every *distinct* pair\nannihilating. Measured exactly in $\\mathbb{Q}(q)$ at $n = 3$ on the\ncorpus's own idempotents: all six off-diagonal entries identically\n$0$, diagonal nonzero, completeness self-test\n$\\sum_\\lambda \\tau(e_\\lambda) = 1$\n([`centre_frobenius_pairing_is_diagonal_probe.py`](../../../computations/probes/centre_frobenius_pairing_is_diagonal_probe.py)).\n\n**Step 4 needs the diagonal form and does not follow from the\nanti-diagonal one.** It argues that $\\phi_q^{(k)}(z_i) \\in Z^{(k)}(A)$\npairs to zero with any $T_w$ whose $Z^{(k)}$-projection vanishes. That\nis precisely $\\langle Z^{(k)}, Z^{(\\ell)}\\rangle = 0$ for\n$k \\neq \\ell$. Under the old anti-diagonal condition the pairing was\nlicensed to be **non**-zero at $\\ell = N - k$, so Step 4's truncation\ndid not follow from Step 1 as written whenever $N - k \\leq\nk_\\star(T_w)$. The correction closes that hole.\n\n**Still open, and not repaired here:** Step 4 pairs a central\n$\\phi_q^{(k)}$ against a general $T_w \\in A$, not against a central\nelement, so \"$T_w$ has zero projection on $Z^{(k)}$\" has to be read as\na statement about $T_w$'s Wedderburn *blocks*. That reading is\nplausible — $e_\\lambda$ central idempotent gives\n$\\tau(e_\\lambda a) = \\tau(e_\\lambda a e_\\lambda)$ — but it is not\nstated in the block, and it is a different question from the one\ncorrected here.",
    },
    {
      kind: "caveat",
      date: "2026-08-26",
      body:
        "Step 1's orthogonality condition was corrected from `k + ℓ ≠ N` (anti-diagonal) to `k ≠ ℓ` (diagonal) — bean `qou-xsv8`. The correction *repairs* Step 4, which needs the diagonal form and did not follow from the anti-diagonal one. The in-prose note states the mathematics; this records the provenance.",
    },
  ],
  uses: [
    "conj:quantum-dilogarithm-stratified",
    "cor:quantum-dilogarithm",
    "prop:categorical-mass-markov",
  ],
  tags: [
    "quantum-dilogarithm",
    "brane-tower",
    "centre-stratification",
  ],
});
