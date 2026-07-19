**Bar on integer scalars**

**Proposition (Lean: `bar_two`).** $\overline 2 = 2$.
*Proof.* $\overline 2 = \overline{1 + 1} = \overline 1 + \overline 1 = 1 + 1 = 2$. $\square$

**Proposition (Lean: `bar_natCast n`).** $\overline n = n$ for every $n \in \mathbb{N}$.
*Proof.* Induction on $n$. Base: $\overline 0 = 0$. Step: $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition (Lean: `isBarSymmetric_natCast n`).** Every natural-number scalar is bar-symmetric.
*Proof.* Restatement of `bar_natCast n` in the `IsBarSymmetric` predicate. $\square$
