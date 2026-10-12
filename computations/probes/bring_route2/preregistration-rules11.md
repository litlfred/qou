# Route 2, option 1d: the two selection rules on every 11-letter braid (pre-registration)

Written 2026-10-11, before anything below was computed. The owner picked "3" that day: pre-register the rules on all 11-letter braids, the length of the real candidates, then see whether either rule's winner is one of the seen braids. Nothing in this file reads Q_β, CODATA, a mass or any target.

## 0. What is already known (read first: this test is NOT clean)

These were seen before this file was written:

- **The q-lengths at t = −q₀ of the seen 11-letter candidates** (`results_qdeformed.md`):
  - nuc11_interleaved = gluon_s0_s0, and gluon_s0_s1: ln q₀ = 0.10434…;
  - class A (gluon_s1_s0, gluon_s1_s1): 2.64959…;
  - nuc11_gen_grouped: 6.57282….
- **Bring lengths of the fresh 11-letter classes** (option 1, `results_option1.json`). The shortest is 4.6031833095…, shared by 24 fresh classes. That is also class A's length.
- **At 13 letters** (option 1c), the smallest q-length was ln q₀. It was attained only by the parabolic braid conjugate to σ₀ followed by full twists, and that braid had no Bring loop.
- **The rule shapes themselves** ("q-length alone" and "Bring loop first") were chosen **after** these numbers were seen. Nothing here can turn either rule into a derived selection principle. A rule that picks a seen braid is a **consistency observation**, not evidence.

What is **not** yet known:
- the q-lengths of the other 11-letter braids;
- whether any hyperbolic 11-letter braid has q-length below ln q₀;
- how many 11-letter braids share the minimum;
- how the 11-letter words group into braids.

## 1. The set

All 2¹¹ positive words in σ₀, σ₁, up to rotation and the σ₀ ↔ σ₁ swap: **94 classes**. This time **nothing is removed**; the seen candidates are included. Words are grouped into braids by conjugacy in B₃, using the key of option 1c (`fibres_probe.s1_key`, with the pre-period parity fix).

## 2. The rules (fixed now)

E_q(w) is the q-length at t = −q₀, as in `preregistration-fibres.md` §1 S4. Positive values only; a braid with E_q = 0 is listed and not ranked.

- **Rule A (q-length alone).** The winner is the braid with the smallest E_q over all 94 classes. It is **decided** when exactly one braid attains the minimum, comparing values to 40 digits.
- **Rule B (Bring loop first).** Take the word classes whose Bring loop is the **shortest** one. "Same loop" is decided by the symmetry rule of `preregistration-sameloop.md` §2, so equal length alone is not enough. Among those, the winner is the braid with the smallest E_q. It is **decided** when exactly one braid attains that minimum.

## 3. What is reported

- For each rule: whether it is decided; the winning braid; and **whether that braid is the braid of a seen candidate**, and which one.
- The full ranking of braids by E_q, with the rank of every seen candidate's braid.
- The braid count, and the number of spellings per braid.

## 4. Checks (pre-registered)

1. **Class count:** 94, by brute force.
2. **Reproduction:** each seen candidate's E_q matches `results_qdeformed.json` to its stored 25 digits.
3. **Reversal:** word reversal maps braid classes to braid classes.
4. **Independent braid key:** for hyperbolic braids, Gauss reduction cycles of the associated binary quadratic forms give the same partition. For parabolic braids, exact reduction to [[1,n],[0,1]] does.
5. **Same loop:** every word class put on the shortest loop is matched to its representative by an explicit symmetry.
6. **Arithmetic:** mpmath, 60 dps for E_q and 30 dps for the Bring geometry; no float64.
