# The one-sided lepton factor in the forced normalisation (2026-11-21)

Thread "Find where the n–p mass error comes from". Owner, 2026-11-21: "Merge. Keep pushing on
lepton." This follows `docs/audits/2026-11-21-qbeta-np-error-budget.md` §11–16 (merged in #8868).
Lean: `QOU/QBeta/ForcedLeptonFactor.lean`.

## Input taken from the eigenphase thread

PR #8836 (`LeptonStrandNormalisation.lean`; probe `qbeta_lepton_normalisation`, check M5) fixes the
lepton normalisation as q^(−2 wr)·Tr(K ρ)/[2]^c, with the lepton strands summed. Three premises
force it: agreement with D1, invariance under an idle strand, and Markov invariance. Over the
1560 γγ words, the unlinked lepton block takes exactly two values:

- e⁻ν̄: fE = (q⁴+1)/(q⁴(q²+1)), which is 0.7432 at q₀;
- mirror e⁺ν: fM = q²(q⁴+1)/(q²+1).

These closed forms come from the probe's exact check, not from a Lean derivation. The premises
are that thread's, for the owner to confirm.

## Results (all exact)

1. **fM = q⁶·fE.** The mirror block is the e⁻ν̄ block times q⁶.
2. **q⁻² − fE = (q²−1)/(q⁴(q²+1)).** So fE < q⁻² for every q > 1, and fE(1) = 1.
   Also **fM > 1** for every q > 1.
3. **Window, for every q, not just q₀.** The unlinked e⁻ν̄ value ε_p·fE lies below ε_n; the
   unlinked mirror value ε_p·fM lies above ε_p. Neither reaches the window (ε_n, ε_p) that a
   decreasing energy map needs (`unlinked_outside_window`). This upgrades audit §16 from a q₀ check
   to a statement about every q in the range. The linked words remain a numerical result (§15–16).
4. **The one-sided placement becomes a rescaling of the scored cell.**
   ε_n − ε_p·fE = −ε_flavour(V³)/(q²(q²+1)) (`fForced_eq`). So
   E₀^full·(ε_n − ε_p fE)/m_e = R(q)/(q²(q²+1)) (`qbetaForced_eq`).
5. **Classical value 3/8, at most 3/8 for every q ≥ 1** (`qbetaForced_one`, `qbetaForced_le`).
   The scored cell has R(1) = 3/4. The forced one-sided reading divides it by q²(q²+1) = 2 at
   q = 1. At q₀ it gives 0.2316·m_e = 0.1183 MeV.

## What it means

Once the lepton normalisation is the forced one, the one-sided placement is no longer a separate
mechanism. It equals the two-sided cell times the electron's own factor 1/(q²(q²+1)), which is
≤ 1/2. The scored cell is already short by the factor 2.404 (audit §3), so this makes the shortfall
larger, about 4.8× at q = 1. The 1.285 MeV near-match of the earlier §11 came only from the
sector-restricted f = q/[2]⁴, which the forced normalisation excludes.

Scope (b) for results 2–5 (exact identities and the inequality R ≤ 3/4). Scope (a) for the
claim that no γγ final state lands in the window: that rests on the 1560-word enumeration.

## What remains open on the lepton

- *Linked words.* Their final-state trace lies in [0.1747, 0.3151] (e⁻ν̄) and [0.4094, 0.5884]
  (mirror), both outside the window. No closed form or bound is proved for them yet.
- *Charged 5-strand vacuum* (option 1 on the eigenphase card). Not computed.
- *Shared placement with a log map* (thread on the E₀/ε→MeV map). There the cell becomes −2c·log q
  for any word, which bypasses the lepton factor entirely.

## Linked words, exact (added 2026-11-21)

Probe `computations/probes/qbeta_lepton_linked_exact/` (preregistered; a scratch run came first,
and the preregistration says so). The 1560 linked words fall into 59 classes by final-state trace.
Each class trace x̂(q) = Tr(K⁹(P_p⊗1)ρ(W))/[2]⁷ is computed as an exact Laurent polynomial in q,
and window crossings are found by exact real-root isolation of x̂ − ε_n and x̂ − ε_p on
q ∈ (1, 23/20].

- All 59 class values reproduce the earlier q₀ values.
- x̂(1) = 3/8 for every class.
- **e⁻ν̄ (24 classes): x̂ < ε_n on the whole range (1, 23/20].** No e⁻ν̄ linked word enters the
  window for any q in range. Scope (b) on this finite set: exact root isolation, no float.
- **Mirror e⁺ν (2 classes enter the window for part of the range):**
  - lepton V3V4V4, junction V1V2V1V2, 27 words: inside for q < 1.10487, x̂(q₀) = 0.40942.
    The boundary sits just below the proton pin 1.10998, which is the 0.0007 near-miss at q₀.
  - lepton V4V5V4V5V3, junction V1V2V1V2, 1 word: inside for q < 1.02211.

These are wrong-charge words for n → p e⁻ ν̄, so they are not a candidate, and nothing is adopted.
The first open item above (linked words) is now closed for e⁻ν̄ on the finite γγ set.
