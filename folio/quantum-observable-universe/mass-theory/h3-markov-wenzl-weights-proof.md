**Proof.** Three steps, each forced.

**Step 1: $y_{(1^3)} \equiv 0$ (Temperley–Lieb quotient).** The Jones
polynomial factors through the Temperley–Lieb algebra
$\mathrm{TL}_n(q)$ (Kauffman bracket), which is the quotient of
$\mathrm{H}_n(q)$ annihilating every $V_\lambda$ with more than two
rows. For $n = 3$ the only such partition is $(1^3)$, so the
Jones-normalised Markov trace assigns it weight zero **identically in
$q$**. Equivalently, the vanishing is the algebraic identity

$$
  [2]_q^{3} - 2\,[2]_q - [4]_q \;=\; 0,
$$

verified by direct expansion: with $[2]_q = q + q^{-1}$,
$[2]_q^3 = q^3 + 3q + 3q^{-1} + q^{-3}$, so
$[2]_q^3 - 2[2]_q = q^3 + q + q^{-1} + q^{-3} = [4]_q$.

**Step 2: Markov normalisation.** $\mathrm{tr}_M(\mathbf{1}_3) = 1$
(the identity braid closes to the 3-component unlink, whose Jones
value is exactly the normalising $[2]_q^2$). With
$d_{(3)}, d_{(2,1)}, d_{(1^3)} = 1, 2, 1$ and Step 1:

$$
  y_{(3)}(q) + 2\, y_{(2,1)}(q) \;=\; 1.
$$

**Step 3: uniqueness from the Borromean closed form.** For
$\beta_{\mathrm{Bor}}$ (writhe $0$, image $\mathrm{id} \in S_3$),
$\chi^{(3)}(\beta_{\mathrm{Bor}}) = 1$ exactly and
$\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$ with
$h = q - q^{-1}$. Substituting Steps 1–2:

$$
  \mathrm{tr}_M(\beta_{\mathrm{Bor}})
  \;=\;
  1 + y_{(2,1)}(q)\,\bigl(\chi^{(2,1)}(\beta_{\mathrm{Bor}}) - 2\bigr)
  \;=\;
  1 - y_{(2,1)}(q)\,\bigl(3h^4 + h^6\bigr).
$$

Comparing with the closed form
$\mathrm{tr}_M(\beta_{\mathrm{Bor}}) = (4 + h^2 - 3h^4 - h^6)/(h^2+4)
= 1 - (3h^4 + h^6)/(h^2 + 4)$, and noting $3h^4 + h^6 \neq 0$ for
$h \neq 0$:

$$
  y_{(2,1)}(q) \;=\; \frac{1}{h^2 + 4} \;=\; \frac{1}{[2]_q^{2}}
  \qquad\text{(uniquely, for all } q \neq 1\text{; at } q = 1 \text{ by continuity)}.
$$

Then Step 2 gives $y_{(3)} = 1 - 2/[2]_q^2 = ([2]_q^2 - 2)/[2]_q^2
= [4]_q / [2]_q^3$ using Step 1's identity. $\square$

**Direction of the argument.** Step 3 determines $y_{(2,1)}$ *from* the
Borromean closed form, which is itself a convention-D object. The step is
therefore a consistency computation internal to convention D, and it is not
evidence for selecting D over the full-Hecke Ocneanu trace (convention C) in
any channel; using it that way would be circular. The independent
characterisation of D is the Temperley–Lieb uniqueness argument
($y_{(1^3)}(z) = 0$ has the unique non-degenerate root $z = q^3/(q^2+1)$), whose premise (that the
relevant fibre functor lands in $\mathrm{Rep}(\mathrm{SU}_q(2)) \simeq
\mathrm{TL}_3$) is a separate question. See the
[trace-convention registry](../../../docs/coordination/trace-convention-registry.md).
