import { proposition } from "../../schema/builders";

/**
 * Each QOU mass-formula coefficient is a shadow price (LP dual
 * variable) of a Frobenius positivity constraint on a single
 * Wedderburn block, not a fitted parameter.
 *
 * This closes the derivation loop:
 *   operator-selection-lp → shadow prices → mass coefficients
 *   (mass-categorical-descent is now a conjecture and is not a dependency)
 *   wedderburn-trace-identity → normalization → trace budget
 *
 * At each Hecke level k, the mass-formula coefficient for
 * partition λ ⊢ k is c_λ = y_λ^* · m_e, where y_λ^* is the
 * optimal dual variable of the Frobenius constraint
 * ⟨Φ, π_λ⟩_F ≥ 0.  The factorisation y_λ^* = C_λ · S_λ(Z,N,A)
 * with q-integer C_λ and content-sum-driven S_λ gives every
 * QOU mass coefficient (across all six terms of
 * conj:six-term-mass-formula-complete) as an algebraic q-rational
 * — no AME-style fitted parameters.
 *
 * History: the block was originally titled
 * `prop:mass-coefficient-shadow-price` framing the claim around
 * the empirical Bethe-Weizsäcker formula.  Renamed 2026-05-18
 * to align with the QOU six-term-mass-formula production
 * framework (the BW framing was superseded by the 2026-05-11
 * plancherel-usage audit which moved the BW-named compute
 * scripts to `_deprecated/`).  The structural claim — shadow
 * price = mass coefficient — is unchanged.
 */
export default proposition({
  label: "prop:mass-coefficient-shadow-price",
  title:
    "Mass-formula coefficients as shadow prices of the Frobenius positivity constraints",
  lean: { ref: "qou:QOU.BraidKnot.MassCoefficientShadowPrice",
    validation: "validated",
  },
  uses: [
    "prop:wigner-coefficient-derivation",
    "prop:operator-selection-lp",
  ],
  tags: [
    "mass-formula",
    "shadow-price",
    "lp-duality",
    "frobenius-positivity",
    "wedderburn",
    "derived-coefficient",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([six-term mass formula](#conj:six-term-mass-formula-complete))" },
    { kind: "caveat", date: "2026-10-11", body: "Two inconsistent definitions of $C_\\lambda$ (bean `qou-wg3c`). `prf:unified-iterative-correction` states $C_\\lambda = m_e\\,H_q(\\lambda)$ (the $q$-hook product), while `prop:mass-coefficient-shadow-price` carries $C_\\lambda = w_\\lambda\\,h/2$ as the class field `C_eq`. At $(2,2)$ these give $6.2893$ MeV and $m_e w h/2 = 0.00887$ MeV; no stated map relates them. Neither is derived: the hook value is asserted universal and fails for six of the seven mass-formula coefficients (`qou-orjl`), and the factorisation $u^*_\\lambda = C_\\lambda S_\\lambda(Z,N,A)$ is a class field the stated LP cannot produce, since its dual constraints carry no $(Z,N)$." },
    {
      kind: "refined-framing",
      date: "2026-09-05",
      body:
        "**O2 applied (owner ruling, 2026-09-05): the statement now says " +
        "*which* program.** It read \"the nuclear operator selection LP\", " +
        "which names `prop:operator-selection-lp` — and that block indexes " +
        "its Frobenius constraints by **NF basis element** ($n!$ of them), " +
        "while this proposition claims a **per-partition** dual ($p(n)$ of " +
        "them; six against three at $n=3$). The two are different programs, " +
        "and the mismatch was never stated. It now is, along with the two " +
        "things that follow: the NF-indexed program\u2019s net-constraint " +
        "dual is identically zero (so any $a_K$ recovered by dividing by it " +
        "is undefined), and the per-partition Frobenius duals are a separate " +
        "question that the committed $H_3$ solve does **not** contradict. " +
        "**No number moves** — per the 2026-08-24 defect audit\u2019s S6, " +
        "the six-term formula runs on the closed-form chirality/writhe route, " +
        "not on the LP; the shadow-price reading is a parallel interpretation. " +
        "Also recorded: `hecke_core_legacy.lp_shadow_price`, named for this " +
        "proposition, solves no program at all — it is the closed form " +
        "$w_\\lambda/d_\\lambda - 1/[k]_q!$, whose subtrahend is " +
        "$\\min_\\lambda(w_\\lambda/d_\\lambda)$ and is not a dual " +
        "variable. Chosen over O3\u2032 (re-pose as a block SDP on the " +
        "radical quotient) only in the sense that O2 is free and " +
        "unconditional; O3\u2032 was authorised in the same ruling and is " +
        "tracked separately. Evidence: PR #6752, " +
        "`docs/proposals/2026-09-05-operator-selection-objective-replacement.md`.",
    },
    {
      kind: "caveat",
      date: "2026-08-22",
      body:
        "**The Frobenius shadow prices are fine at $H_3$; the *net-constraint* " +
        "one is identically zero, and that is what the $a_K$ extraction " +
        "divides by.** Two separate things, and an earlier note in bean " +
        "`qou/8na1` conflated them — corrected there. (i) The " +
        "partition-indexed LP (`a-K-via-lp-dual-full.witness.json`, proton) " +
        "gives $y^*_{[3]} = y^*_{[2,1]} = 1.0$, $y^*_{[1,1,1]} = 0$, so " +
        "$c_\\lambda = y^*_\\lambda m_e$ is **not** contradicted and the " +
        "factorisation $u^*_\\lambda = C_\\lambda S_\\lambda$ is satisfiable " +
        "with $S_\\lambda$ a unit on both nonzero blocks. (ii) The " +
        "net-constraint dual $y_0^*$ is **exactly zero** — forced in " +
        "$\\mathbb{Q}(q)$ by the trace-form radical (Lean: " +
        "`y_0_eq_zero_of_radical`), confirmed by both committed f64 solves — " +
        "so the dual objective $n_{\\mathrm{target}} \\cdot y_0^*$ vanishes " +
        "for every target, and every extraction routing $a_K$ through it " +
        "($a_K^{\\mathrm{dual\\_ratio}}$, $a_K^{\\chi\\text{-active}}$) is " +
        "undefined. Both scripts return `null` and record why; the guard is " +
        "firing on a structural identity, not on noise. **The open question " +
        "is whether $a_K$ is recoverable from this LP at all**, not whether " +
        "the coefficients vanish. Second, independent thread: " +
        "`aK_via_lp_dual_full.py` reports that *\"under convention D the " +
        "$\\ell(\\lambda) \\ge 3$ blocks vanish identically, so this LP needs " +
        "re-posing on the two-row quotient\"* — which is why $[1,1,1]$ is " +
        "zero above, and nobody has re-posed it. `validation` left at " +
        "`validated`: the Lean is a §3b conditional carrier whose `factor` " +
        "field is a hypothesis, its three theorems are sorry-free " +
        "consequences, and nothing here shows the class uninhabited.",
    },
    {
      kind: "note",
      date: "2026-06-22",
      body:
        "The charge-type scaling function $S_\\lambda$ (left here as \"Z-dependent\") is identified — formalize-first, no fit — with the free-vs-atom **$H_{3A}$ q-Reeb phase** $|\\Delta\\theta_\\lambda|$, not a partition-only $Z(Z-1)$ count. The bare $\\sum_{\\text{charge}} C_\\lambda\\,Z(Z-1)\\,m_e$ misses the $^3$H$-^3$He split by $22.6\\times$ (the GAP-A-4 $H_3$-collapse obstruction: $p\\equiv n\\equiv{}^3$He at $H_3$); the atomic q-Reeb phase reproduces it to $\\sim118\\%$ (right order). The Coulomb channel $\\sinh(\\log q)=h/2$ is already the factor in $C_\\lambda=\\tilde w_\\lambda\\,h/2$. See `docs/audits/2026-06-22-charge-slambda-reeb-phase-crack.md`.",
    },
  ],
});
