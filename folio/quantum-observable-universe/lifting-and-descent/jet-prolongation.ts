import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-prolongation",
  lean: { ref: "qou:QOU.JetProlongation", validation: "not_checked" },
  title: "Jet Prolongation",
  tags: ["jet-bundle", "frobenius-hopf", "prolongation"],
  examples: ["ex:jet-prolongation-su2", "rem:prolongation-categorical", "ex:brane-tower-levels"],
  uses: ["def:quantum-observable-universe", "def:categorical-jet"],
  proofs: ["prf:jet-prolongation"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-22",
      body:
        "Owner ruling 2026-11-22: the prolongation object is the tangent algebra " +
        "$T(A) = \\mathrm{Sym}_A(\\Omega^1_{A/R})$, not $J^1(A)$. The splitting $r \\circ \\ell = \\mathrm{id}_A$ " +
        "of the structure map and the augmentation is formalised " +
        "(`QOU.LiftingDescent.tangentRetract_comp_tangentSection`, " +
        "`QOU/LiftingDescent/TangentAlgebraSplitting.lean`, sorry-free). Cited, not formalised: for " +
        "$A = \\mathcal{O}(G)$, $T(A) = \\mathcal{O}(TG)$ with $TG = G \\ltimes \\mathrm{Lie}(G)$ a group, so " +
        "$T(A)$ is a commutative Hopf algebra and both maps are Hopf maps. Still open: the Frobenius form " +
        "and the vanishing condition on $T(A)$. The proof's step deriving them from $A$ being a direct " +
        "summand is not a valid argument, and for compact $G$ the group $TG$ is not compact, so no " +
        "Haar-normalised integral is available. Non-commutative case: the two-sided jet " +
        "$A \\ltimes M$ splits (`QOU/LiftingDescent/NoncommJet.lean`), and a square-zero skew-primitive " +
        "escapes the characteristic-zero obstruction (`QOU.LiftingDescent.skewPrimitive_sq`); for " +
        "$A = k[\\mathbb{Z}/2]$, $A \\ltimes \\Omega^1_u(A)$ has Sweedler's four-dimensional Hopf presentation " +
        "(cited). Sweedler's algebra itself is formalised as a Hopf algebra over any commutative ring " +
        "(`QOU.LiftingDescent.Sweedler.instHopfAlgebra`, `QOU/LiftingDescent/SweedlerJet.lean`, sorry-free), " +
        "with an algebra map into any square-zero extension $A \\ltimes M$ from an involution $g$ and an " +
        "element $m$ with $m g = -g m$ (`Sweedler.toJet`). That the map is an isomorphism onto " +
        "$k[\\mathbb{Z}/2] \\ltimes \\Omega^1_u$ is not formalised.",
    },
    {
      kind: "caveat",
      date: "2026-11-22",
      body:
        "The Frobenius–Hopf inheritance is false for $J^1(A) = (A \\otimes A)/I^2$ in the commutative " +
        "characteristic-zero case. Proved (scope b, invariant: a square-zero primitive vanishes in " +
        "characteristic zero): for $A = k[X]$ with $X$ primitive, no multiplicative comultiplication on " +
        "$J^1(A)$ makes both jet sections $a \\mapsto [a \\otimes 1]$ and $a \\mapsto [1 \\otimes a]$ " +
        "compatible (`QOU.LiftingDescent.jet_polynomial_no_bialgebra`, " +
        "`QOU/LiftingDescent/JetNoBialgebra.lean`, sorry-free). Cited, not formalised: by Cartier's " +
        "theorem (Waterhouse 1979, §11.4) a commutative Hopf algebra over a field of characteristic zero " +
        "is reduced, while $I/I^2 \\subset J^1(A)$ is a nonzero square-zero ideal whenever " +
        "$\\Omega^1_{A/k} \\neq 0$. So for $A = \\mathcal{O}(\\mathrm{SU}(2))$ no commutative Hopf structure " +
        "exists on $J^1(A)$ at all. Not excluded: a non-commutative or braided ($q \\neq 1$) setting, " +
        "and a different jet object such as the tangent-bundle algebra $\\mathrm{Sym}_A(\\Omega^1_A)$.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-22",
      body:
        "On the owner ruling of 2026-11-22 the jet object is $(A \\otimes A)/I^2$, $I = \\ker m$. That " +
        "object contains $A$ as a direct summand (`lem:jet-prolongation-categorical-jet`), which the old " +
        "$A \\otimes \\Omega^1(A)$ did not. The Frobenius–Hopf inheritance is still open for the new object: " +
        "for a commutative Hopf algebra $I$ is a Hopf ideal, but $I^2$ is not a coideal in general, so " +
        "$(A \\otimes A)/I^2$ is not obviously a quotient bialgebra.",
    },
    {
      kind: "caveat",
      date: "2026-11-21",
      body:
        "The proof cites `lem:jet-prolongation-categorical-jet` for the claim that $J^1(A)$ inherits " +
        "$(\\Delta', \\varepsilon', S')$ from $A$. That claim was retracted on 2026-11-21: restricting " +
        "$\\Delta$ to $\\Omega^1(A)$ fails for every bialgebra with $m$ not injective " +
        "(`rem:jet-comul-does-not-restrict`). That step of the proof is open until a Frobenius–Hopf " +
        "structure on $J^1(A)$ is supplied some other way.",
    },
  ],
});
