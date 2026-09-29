---
# qou-hft3
title: He-4 disjoint-product identity fails 5.94x once the 480s timeout stops masking it
status: completed
type: bug
priority: normal
created_at: 2026-09-06T10:41:05Z
updated_at: 2026-09-06T11:14:33Z
---

## What happened

`computations/atomic_tr_m_helium4.py` cross-checks two routes to |tr_M(⁴He)| on
H₁₂:

- **(A) disjoint product** — `|tr_M(⁴He)| = |tr_M(p)|² · |tr_M(n)|²`, read from
  `atomic-tr-m-mpfr-50dps-proton.witness.json`
- **(B) direct recursion** — `markov_trace_recursive.markov_trace_of_word(12, word)`

The **committed** witness records (B) as having never run:

    direct_recursion.error                          = "timeout_after_480s"
    direct_recursion.elapsed_sec                    = 480.00026202201843
    direct_recursion.abs_tr_M_50dps                 = null
    direct_recursion.matches_disjoint_product_within_1ppb = null

On 2026-09-06 it completed in **16.54 s** and the two routes disagree:

    (A) disjoint product   |tr_M(⁴He)| = 1.280783151528646
    (B) direct recursion   |tr_M(⁴He)| = 7.610469960740114
        ratio  (B)/(A)                 = 5.9420
        Δ                              = 4.94204

The producer prints `✗ MISMATCH — investigate disjoint-product application on
H_12` and then **exits 0** ("0 assertions, all passed"). The mismatch is
printed, not asserted, so nothing downstream notices.

So the identity has never once been verified. `matches_..._within_1ppb: null`
reads as "not checked"; it was in fact "checked and cannot pass", and the
timeout hid which.

## Why it suddenly completes

Not the row-cap optimisation landed in the same pass (`qou-fq0f`, ~100x on the
Wenzl bridge): this producer uses `markov_trace_of_word`, an independent
recursion, and imports the bridge nowhere. It went from >480 s to 16.5 s for
some other reason — a sibling's merged work today, or machine variance. Worth
confirming, because if it is variance the timeout can come back and re-hide
this.

## Three things to separate before fixing

1. **Which arm is wrong.** A factor of 5.942 is not a precision artefact. Note
   the disjoint-product arm squares values it did not compute.
2. **The word is not the canonical one.** It is hand-specified —
   `σ₁⁷σ₂⁴ · σ₄⁷σ₅⁴ · σ₇⁶σ₈⁴σ₇⁻¹ · σ₁₀⁶σ₁₁⁴σ₁₀⁻¹`, 44 crossings — not
   `atom_braid_word_3A(2,2)`, so this "helium-4" is a different braid from the
   one the intra-ordering ruling (`qou-hu1f`) governs. Its inputs are also
   grouped-era: `abs_tr_p = 1.1457596924573` is the **superseded grouped**
   proton value; the ruling gives 0.62932842249. Whatever (A) and (B) are
   comparing, it is not the production ⁴He.
3. **A printed ✗ must not exit 0.** That is the defect that let this sit.

## Now reachable, which changes the options

`qou-fq0f` made the Wenzl bridge run at H₁₂ in **19.4 s** (previously
unreachable), and `atomic_tr_m_helium4.py`'s own header already anticipates
this: line 25 says it should move to `tr_M_via_wenzl_bridge_mpfr.py` "once the
y-lambda witness is extended". It is extended and the bridge is fast. A **third,
independent** value for |tr_M(⁴He)| is now cheap to obtain, which is the natural
way to settle which of (A) and (B) is wrong rather than arguing from the two
that disagree.

Direct bridge evaluation on the canonical word `atom_braid_word_3A(2,2)` gives
`0.01123741765976742156419955` in 19.37 s — but that is the canonical borromean
word, so it is not directly comparable to either arm above until item 2 is
resolved. Recorded here as the starting point, not as the answer.

## Also

`atomic-tr-m-helium4.witness.json` emits 2 raw-float64 fields
(`direct_recursion.budget_sec`, `.elapsed_sec`) — flagged by the raw-float64
gate on every run, and inert only because they are timings.

## Cross-validation: neither arm is near the canonical value

Landed with the row cap in the same pass. Two independent routes to
|tr_M(⁴He)| on the **canonical** word `atom_braid_word_3A(2,2)` at H₁₂ agree to
full precision:

    direct Wenzl-bridge evaluation      0.01123741765976742156419955
    binding_canonical.py (regenerated)  0.011237417659767421564

Both differ from **both** arms of `atomic_tr_m_helium4.py` (1.2808 and 7.6105)
by two orders of magnitude. That strongly supports item 2 above: the word this
producer uses — hand-specified, 44 crossings — is not the production ⁴He braid,
so its two arms are disagreeing about something that is not the quantity the
paper needs. Settle the word before adjudicating the arms.

Only computable at all because the row cap made H₁₂ reachable (19.4 s from
previously unreachable).

## RESOLVED 2026-09-06

The question "which arm is right?" had no answer, because **both arms trace the
disjoint word**. Item 2 above was the whole of it.

    |tr_M(4He)| = 0.011237417659767421564199549374410607269662696081261

Three structurally independent routes, agreeing to 51 digits at the proton pin:

| route | what it is | time |
|---|---|---:|
| Wenzl bridge on `atom_braid_word_3A(2,2)` | Hoefsmit seminormal + Wenzl weights at H₁₂ | ~17 s |
| `markov_trace_canonical` | Markov-axiom recursive reducer | ~1 s |
| `closed_form_tau_M`, `bring_color_weighted` | Phase 5q closed form | 0.002 s |

The first two agreeing **is** the Schur-Weyl identity `Σ_λ y_λ χ^λ = tr_M`
holding on the canonical word — the test the disjoint word fails by ~5, the
same failure PR #564 measured on the deuteron.

The third also discriminates the pn convention without assuming it:
`bring_color_weighted` matches to 30 digits, `chi_lambda_braid` and `uniform`
give 0.013547 (20 % off). Independent confirmation of the owner's 2026-08-15 R3
ruling.

**What was actually blocking it** was not tractability. The module's own header
prescribed this fix and named its precondition; the row cap (`qou-fq0f`) met it.
`canonical_tr_m_helium4_stub.py`'s intractability estimate was wrong in both
factors it cited — 70 of its 77 partitions carry weight identically zero, and
its "max dim 7700" is (5,3,2,1,1), a five-row shape the cap annihilates.

**Arm (B) can never be run on the canonical word.** `markov_trace_of_word`
takes jet-tracker signed integers, which express σ and σ⁻¹ only; the canonical
word carries the uniform pn interface -h/2 (×8) and one Bring colour-weighted
interface. Not a budget problem — an input-format one.

Follow-up opened: **`qou-y2o7`** — `compute_tau_M_nucleon_H3` is locked to the
grouped ordering by its monotone-only χ kernel, and 18 consumers inherit it.

### Correction to the table above — which routes are independent of what

The commit message and the table say the second route is
`markov_trace_canonical`, "a structurally independent Markov-axiom reducer".
That is wrong on both counts and the distinction matters.

`binding_canonical.py` *imports* `markov_trace_canonical.tr_M_element` but its
witness records `use_closed_form: False, use_transfer: True`, so it ran
`tr_m_atom_via_transfer.tr_m_atom_zn` — the fine-Bratteli transfer matrix,
which is another evaluation of **Σ_λ y_λ χ^λ**, not a Markov-axiom reduction.

So the three routes are not three independent claims:

| route | what it evaluates | independent of |
|---|---|---|
| Wenzl bridge | Σ_λ y_λ χ^λ, Hoefsmit seminormal matrices | the transfer implementation |
| fine-Bratteli transfer | Σ_λ y_λ χ^λ, transfer sweep | the bridge implementation |
| `closed_form_tau_M` | τ_p^Z · τ_n^N · ∏ f_i — a **different structural claim** | both |

The first two are independent *implementations* of one identity; their
agreement validates the code, not the mathematics. The load-bearing result is
that the **closed form**, which asserts multiplicativity along the chain,
agrees with both to 27+ digits at A = 4 — that is the multiplicative ansatz
being confirmed by a direct H₁₂ character sum, and it is what the original
claim should have said.

Nothing computed changes; the value and the digit counts stand.
