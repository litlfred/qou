import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mi-sw-abelianisation",
  lean: { ref: "qou:QOU.Brings.mi_sw_abelianisation",
    validation: "stub",
  },
  title: "Abelianisation of the MI integral on exceptional divisors",
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-08",
      body:
        "Lean status corrected from `not_checked` to `trivial` (bean qou-slpd). " +
        "The file builds and is sorry-free — that part was never in doubt, it " +
        "had simply not been checked. What checking it showed is that the " +
        "declaration carries NO mathematical content: " +
        "`theorem mi_sw_abelianisation (_bs) (n) (sw_period mi_integral : ℕ → ℝ) " +
        "(fake_flat_abelian : ∀ k, mi_integral k = sw_period k) : " +
        "mi_integral n = sw_period n := fake_flat_abelian n`. The hypothesis IS " +
        "the conclusion, universally quantified; the proof is a projection. The " +
        "entire claim — that fake-flatness forces abelianisation on the " +
        "exceptional divisor, so the MI integral reduces to the SW period — is " +
        "ASSUMED as `fake_flat_abelian`, not derived. Per the schema, `trivial` " +
        "is the enum value for a trivially-true lemma, so that is now what the " +
        "field says. This matters because the block sits upstream of the " +
        "keystone `conj:qdifference-kernel-prolongation-symbol` via its `uses[]`; " +
        "the keystone's premises should not read as Lean-backed when one of them " +
        "is a restatement. Discharging it means proving the abelianisation, i.e. " +
        "steps (1)-(3) of the proof outline in `QOU/BringsSurface.lean`, not " +
        "assuming their conclusion.",
    },
    {
      kind: "status",
      date: "2026-08-08",
      body:
        "**Restated as a class with no instance** (bean qou-kyst; owner said " +
        "proceed). `QOU/BringsSurface.lean` now declares " +
        "`class MISWAbelianisation (sw_period mi_integral) : Prop` with the " +
        "abelianisation as its single field, and `mi_sw_abelianisation` derives " +
        "the conclusion from `[K : MISWAbelianisation …]`. This is how the " +
        "corpus already carries its other open content-bearing claims (§3b-tax, " +
        "cf. `QDifferenceKernelIsProlongationSymbol`). The difference from the " +
        "old form is not cosmetic: the previous theorem could be discharged by " +
        "handing it its own conclusion, whereas an instance must now exhibit " +
        "the abelianisation. The open state is in the type. `validation` moved " +
        "`trivial` → `stub`, which is the enum value for a declaration whose " +
        "content is not supplied. Mathlib cannot support a real instance — " +
        "principal bundles over S², nonabelian gauge theory, Yekutieli " +
        "multiplicative integration — so no-instance is expected to persist; " +
        "what has changed is that it is now stated rather than disguised.",
    },
  ],
  uses: [
    "rem:brings-smoothness",
    "def:mass-identity",
    "rem:weight-space-decomposition",
    "rem:color-tube-cubic",
  ],
  proofs: ["prf:mi-sw-abelianisation"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/mi-sw-abelianisation-0.svg", blockIndex: 0, hash: "af7757ccd6f4" },
  ],

});
