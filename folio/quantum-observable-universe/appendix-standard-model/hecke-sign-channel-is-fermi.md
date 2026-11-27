**Proposition.** Let two strands be labelled by $\{1,\dots,n\}$ and let $\sigma$ act on
$V \otimes V$, $V = K^n$, by the standard braiding
$\sigma(e_i \otimes e_i) = q\, e_i \otimes e_i$, $\sigma(e_i \otimes e_j) = e_j \otimes e_i$ and
$\sigma(e_j \otimes e_i) = e_i \otimes e_j + (q - q^{-1})\, e_j \otimes e_i$ for $i < j$. Then

1. $\sigma^2 = (q - q^{-1})\sigma + 1$, so $\sigma$ has eigenvalues $q$ and $-q^{-1}$;
2. if $q^2 + 1 \neq 0$, a pair state $x = \sum_{k,l} f_{kl}\, e_k \otimes e_l$ satisfies
   $\sigma x = -q^{-1} x$ if and only if $f_{kk} = 0$ for all $k$ and
   $f_{lk} = -q^{-1} f_{kl}$ for $k < l$;
3. $\sigma x = q x$ if and only if $f_{lk} = q f_{kl}$ for $k < l$; every diagonal state
   $e_i \otimes e_i$ lies in this channel;
4. at $q = 1$ the $-q^{-1}$ channel is the Fermi condition $f_{ji} = -f_{ij}$ of
   [`prop:fermi-pair-wedge`](fermi-pair-wedge.md).

Item 2 excludes equal labels for every $q$ with $q^2 + 1 \neq 0$, not only at $q = 1$.

**Proof.** Each item is a direct computation on the coefficients $f_{kl}$, split by the cases
$k < l$, $k = l$, $k > l$. For item 2 on the diagonal, $q f_{kk} = -q^{-1} f_{kk}$ gives
$(q + q^{-1}) f_{kk} = 0$, and $q(q + q^{-1}) = q^2 + 1 \neq 0$. $\square$

**Scope.** The braiding gives the two channels and their content. It does not choose
between them: that a matter strand pair lies in the $-q^{-1}$ channel is still an input.
With that input, every result of [`prop:fermi-pair-wedge`](fermi-pair-wedge.md) is a
statement about the $-q^{-1}$ eigenspace of $\sigma$.
