# Route 2, option 1d: results

Recipe: `preregistration-rules11.md`, committed (25c77a0265) before this run. Producer: `rules11_probe.py`. The braid keys use exact integer and sympy arithmetic. q-lengths use mpmath at 60 dps, with q₀ the proton pin. The Bring geometry uses mpmath at 30 dps. **6/6 checks pass.** No Q_β, CODATA or mass input.

**Read §0 of the pre-registration first.** The seen candidates' q-lengths were known before this run, so §2 below is a consistency observation, not evidence.

## 1. How the 11-letter words collapse

- There are **94** classes of positive 11-letter words (up to rotation and the σ₀ ↔ σ₁ swap). They form **16** braids (conjugacy classes in B₃).
- Every braid has positive q-length at t = −q₀, so none is excluded.
- Bring-loop status is constant on each braid.
- Nine braids have a Bring loop. Seven have none, because their image in Δ(2,4,5) is parabolic or elliptic.

The six seen 11-letter candidates fall into three braids:

| braid (S1 key) | spellings | E_q = q-length at −q₀ | rank | Bring loop length L | seen candidates |
|---|---|---|---|---|---|
| parabolic, n = −1 (σ₀Δ² up to conjugacy) | 30 | 0.10434072031951951231… = ln q₀ | **1** | none | nuc11_interleaved, gluon_s0_s0, gluon_s0_s1 |
| hyperbolic, tr 4 | 25 | 2.64958798946969731163… | **4** | 4.6031833095… (shortest) | gluon_s1_s0, gluon_s1_s1 (class A) |
| hyperbolic, tr 26 | 1 | 6.57282073719148121302… | **15** of 16 | 6.3676503714… | nuc11_gen_grouped |

The ranks 2 and 3 are parabolic braids with no loop (E_q = 5·ln q₀ and 11·ln q₀). On a parabolic braid, E_q = |n|·ln q₀.

## 2. The two rules

**Rule A (q-length alone): decided.**
- The winner is the parabolic braid, with E_q = ln q₀.
- **It is the braid of nuc11_interleaved**, the element the dashboard scores. gluon_s0_s0 and gluon_s0_s1 are spellings of the same braid.
- It has no Bring loop.

**Rule B (shortest Bring loop first, then q-length): decided.**
- The shortest loop has L = 4.603183309507916659974173. It carries 26 word classes, which the symmetry rule confirms are all one loop.
- Those 26 word classes are two braids:
  - the tr-4 braid, 25 spellings, E_q = 2.6496…;
  - the tr-16 braid, 1 spelling, E_q = 5.6055….
- The winner is the tr-4 braid. **It is the braid of class A** (gluon_s1_s0 / gluon_s1_s1).

**Each rule picks a seen candidate's braid, and they pick different ones.** This is the same split as the 13-letter run (option 1c), now on the real candidates' length.

## 3. What this does and does not show

- **It does not choose between the rules.** Both shapes were chosen after the seen q-lengths were known (pre-registration §0). The question "q-length alone, or Bring loop first?" is a decision about what the selection principle is (bean qou-99qc). These numbers cannot make it.
- **It does show that both rules are decided at 11 letters**, with a unique winner and no ties at 40 digits.
- **Each rule's winner is the braid of a seen candidate.** That is a consistency observation for both, not a distinction between them.
- **nuc11_gen_grouped ranks 15th of 16 under Rule A, and is not on the shortest loop.** Neither rule favours it.
- **"The word" is a braid, not a spelling.** Each rule picks a braid, which has 30 or 25 positive spellings. Choosing among spellings of one braid would need an invariant that is not a conjugacy invariant. Neither rule here supplies one.
