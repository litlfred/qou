*Proof.*
Define the **diagonal function**

$$
  d(n) \;=\; \mathrm{eval}(e(n))(n) + 1.
$$

For any program $p \in P$, surjectivity gives $n$ with
$e(n) = p$.  Then

$$
  d(n) = \mathrm{eval}(p)(n) + 1 \neq \mathrm{eval}(p)(n),
$$

so $d \neq \mathrm{eval}(p)$.  Since $p$ was arbitrary,
$d \notin \mathrm{im}(\mathrm{eval})$. $\square$

**Necessity of $\mathbb{N}$-embedding.**

The diagonal argument constructs $d$ by evaluating program
$e(n)$ on input $n$ --- self-application.  This requires:

1. **Countability of programs**: $e$ surjects from $\mathbb{N}$
   onto $P$, so programs can be indexed by natural numbers.
   For the QOU, this holds because the braid group $B_n$ on
   $n$ strands is finitely generated, hence countable, and the
   set of all finite braids $\bigsqcup_n B_n$ is a countable
   union of countable sets.

2. **$\mathbb{N}$ as input domain**: programs compute functions
   $\mathbb{N} \to \mathbb{N}$, meaning the system can
   represent and operate on natural numbers.  In the QOU, this
   is the content of Turing completeness
   ([Skein Turing machine](#rem:skein-turing-machine)): each
   Toffoli gate acts on bit strings (elements of
   $\{0,1\}^n \hookrightarrow \mathbb{N}$), and the
   Skein polynomial evaluates to a value distinguishing
   different inputs.

If either condition fails --- if programs are uncountable, or
if the system cannot represent $\mathbb{N}$ --- then the
diagonal construction does not apply and the computable
fragment may equal the full function space.  A trivial
category (one object, one morphism) is vacuously
"Turing-complete" but has no non-computable sections because
it cannot encode arithmetic.

**Connection to the computational horizon.**

Each non-computable function $d$ corresponds to a section
$E_d \in \Gamma(\mathcal{S}, A_0)$ that does not factor
through any finite braid
([non-computable bundles](#rem:skein-turing-machine)).  These
sections populate the computational horizon
$\mathcal{H}_c = V(\mathfrak{h}_c)$
([computational horizon](#def:computational-horizon)):

$$
  E_d \in
  \Gamma(\mathcal{S}, A_0)
  \setminus
  \Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)
  \quad\Longrightarrow\quad
  \mathcal{H}_c \neq \varnothing.
$$

The proposition guarantees that such $E_d$ exist whenever the
system satisfies arithmetic non-triviality.  The
computational horizon is therefore a **necessary feature** of
any Turing-complete resolution system with $\mathbb{N}$-embedding
--- not a contingent property of particular NP-complete links,
but a consequence of the system's expressive power.
