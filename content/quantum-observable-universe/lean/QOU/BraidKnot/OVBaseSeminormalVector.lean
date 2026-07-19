import QOU.BraidKnot.JucysMurphy

/-!
# OV base seminormal vector — the polytabloid JM computation (toward `seminormalVector_base_exists`)

The single remaining `sorry` in the Okounkov–Vershik seminormal cone,
`seminormalVector_base_exists` ([`JucysMurphy.lean`]), reduces (numerically confirmed,
[audit 2026-07-19](../../../../docs/audits/2026-07-19-ov-base-vector-column-superstandard-verification.md))
to the eigen-equation on the **column-superstandard** polytabloid:

  `X_s · e_{T₀} = content(cell of s) · e_{T₀}`.

This file builds that computation from the sorry-free Specht foundation. First brick:
the **reduction** of the abstract JM action `(rep μ).asAlgebraHom (jucysMurphy n s)`
applied to a polytabloid into the concrete signed-cell polytabloid sum
`∑_{j<s} e_{(j\,s)·t}` — general in the tableau `t`, from
`Representation.asAlgebraHom_single` + `rep_polytabloid`.

-- Ref: [vershik-kerov1977] (Young's seminormal form)
-/

namespace QOU.BraidKnot.OVBaseSeminormalVector

open Specht QOU.BraidKnot.JucysMurphy

variable {k : Type} [CommRing k] {μ : YoungDiagram}

/-- **JM action on a polytabloid = a polytabloid sum.** The Jucys–Murphy element
    `X_s = ∑_{j<s} (j\,s)` acts on the polytabloid `e_t` by
    `∑_{j<s} e_{(j\,s)·t}` — each transposition permutes the polytabloid
    (`rep_polytabloid`), and `asAlgebraHom` sends the `single` sum to the
    endomorphism sum. General in `t`; the eigen-equation is what this sum collapses
    to for the column-superstandard `T₀`. -/
theorem jm_smul_polytabloid (s : Fin (Specht.nOf μ)) (t : Specht.Tableau μ) :
    (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s)
        (Specht.polytabloid (k := k) t)
      = ∑ j ∈ Finset.univ.filter (fun j : Fin (Specht.nOf μ) => j.val < s.val),
          Specht.polytabloid (k := k) ((Equiv.swap j s) • t) := by
  unfold jucysMurphy
  rw [map_sum, LinearMap.sum_apply]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  rw [Representation.asAlgebraHom_single, one_smul,
    QOU.BraidKnot.JucysMurphy.rep_polytabloid]

end QOU.BraidKnot.OVBaseSeminormalVector
