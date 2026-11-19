import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:n-v-bring-action",
  title: "S_5 action on H_n(q) at the electroweak slice",
  cites: ["bring1786", "klein1888"],
  uses: [
    "prop:brings-is-qou",
    "def:hyperelliptic-quintic",
    "conj:mass-endomorphism",
  ],
  defines: [],
  tags: ["tier:E", "n-v", "electroweak", "bring", "s5", "substrate-axiom"],
  lean: { ref: "qou:QOU.Observations.NVBringAction" },
  authorNotes: [
    {
      kind: "status",
      body: "**Conjectural.**  This is a substrate axiom in the precise sense\nof [`AGENTS.md` §3b](../../../AGENTS.md#3b-conjectural-propagation):\nthe categorical $S_5$-action on $H_n(R, q)$ at the EW slice is\nasserted but not formally constructed.  It is the **first** of the\ntwo lemmas in the\n[N_v derivation](#conj:n-v-leading-order-derivation) chain;\ncombining it with\n[the EW-slice depth lemma](#conj:n-v-tower-depth-ninety) gives the\nleading-order closure $N_v = 120 \\cdot q_0^{90}$ (residual $-0.58\\%$\nvs CODATA Higgs VEV).",
    },
      {
      kind: "status",
      date: "2026-09-03",
      body:
        "**The Lean sibling did not compile, and had not for some time.** " +
        "`\u03a3` is Lean 4 notation for `Sigma` and cannot be used as a binder " +
        "name; every declaration in the file used it, giving **8 parse errors, " +
        "exit 1**. Nothing imports this file (a content-block sibling sits " +
        "outside the Lake globs) and CI is dispatch-only here, so nothing was " +
        "looking. Renamed the binder to `slice`, which then revealed **3 " +
        "further errors the parse failures had masked** \u2014 `opaque \u2026 : \u211d` needs " +
        "`Inhabited \u211d`, and the file imported neither `Mathlib.Data.Real.Basic` " +
        "nor anything providing it. With that import the file is **exit 0, zero " +
        "errors, zero warnings** for the first time.",
    },
    {
      kind: "refined-framing",
      date: "2026-09-03",
      body:
        "**The class was being discharged by a global instance from a global " +
        "axiom, which defeated it entirely.** The file carried " +
        "`axiom s5_acts_on_ew_slice` plus " +
        "`instance instance_from_axiom (slice) : NVBringAction slice where " +
        "rescale_eq := s5_acts_on_ew_slice slice`. Instance resolution then " +
        "supplies `[NVBringAction slice]` silently, so a downstream author who " +
        "omits the hypothesis gets an axiom-backed theorem whose **statement is " +
        "identical** to the conditional one. Measured, on two theorems with the " +
        "same statement written each way: with the hypothesis, " +
        "`[propext, Classical.choice, Quot.sound]`; without it, the same plus " +
        "`QOU.Observations.s5_acts_on_ew_slice`. AGENTS.md \u00a73b-tax is explicit " +
        "\u2014 an unproved primary is a content-bearing class with **no instance**, " +
        "and one must not fabricate a trivial instance to close it. Both the " +
        "axiom and the instance are removed; `rescale_EW_eq_120` now takes " +
        "`[inst : NVBringAction slice]`. The file is **axiom-free**, and the " +
        "unconditional form now fails to elaborate " +
        "(`failed to synthesize NVBringAction slice`) rather than compiling " +
        "silently \u2014 the loophole is closed by construction, not by convention. " +
        "Constructing a genuine instance (deriving the S\u2085 action rather than " +
        "assuming it) is the open work, bean `qou-5lib`.",
    },
],
  computation: {
    engine: "mpmath",
    script: "computations/sigma_f_electron_shell_chain.py",
    witness: "computations/sigma-f-electron-shell-chain.witness.json",
    status: "verified",
  },
});
