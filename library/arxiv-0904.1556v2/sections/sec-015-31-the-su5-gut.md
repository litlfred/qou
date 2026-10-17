---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-015-31-the-su5-gut
section_title: "The SU(5) GUT"
section_number: 3.1
pages: 32-42
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:su(5) label="sec:su(5)"}

The ${\rm SU}(5)$ grand unified theory appeared in a 1974 paper by Howard Georgi and Sheldon Glashow [@{GeorgiGlashow:su(5)}]. It was the first grand unified theory, and is still considered the prototypical example. As such, there are many accounts of it in the physics literature. The textbooks by Ross [@ross:gut] and Mohapatra [@mohapatra:us] both devote an entire chapter to the ${\rm SU}(5)$ theory, and a lucid summary can be found in a review article by Witten [@witten:grandunification], which also discusses the supersymmetric generalization of this theory.

In this section, we will limit our attention to the nonsupersymmetric version of ${\rm SU}(5)$ theory, which is how it was originally proposed. Unfortunately, this theory has since been ruled out by experiment; it predicts that protons will decay faster than the current lower bound on proton lifetime [@pati:decay]. Nevertheless, because of its prototypical status and intrinsic interest, we simply must talk about the ${\rm SU}(5)$ theory.

The core idea behind the ${\rm SU}(5)$ grand unified theory is that because the Standard Model representation $F \oplus F^*$ is 32-dimensional, each particle or antiparticle in the first generation of fermions can be named by a 5-bit code. Roughly speaking, these bits are the answers to five yes-or-no questions:

-   Is the particle isospin up?

-   Is it isospin down?

-   Is it red?

-   Is it green?

-   Is it blue?

There are subtleties involved when we answer 'yes' to both the first two questions, or 'yes' to more than one of the last three, but let us start with an example where these issues do not arise: the bit string $01100$. This names a particle that is down and red. So, it refers to a red quark whose isospin is down, meaning $-\frac{1}{2}$. Glancing at Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"}, we see just one particle meeting this description: the red left-handed down quark, $d^r_L$.

We can flesh out this scheme by demanding that the operation of taking antiparticles correspond to switching 0's for 1's in the code. So the code for the antiparticle of $d^r_L$, the 'antired right-handed antidown antiquark', is $10011$. This is cute: it means that being antidown is the same as being up, while being antired is the same as being both green and blue.

Furthermore, in this scheme all antileptons are 'black' (the particles with no color, ending in 000), while leptons are 'white' (the particles with every color, ending in 111). Quarks have exactly one color, and antiquarks have exactly two.

We are slowly working our way to the ${\rm SU}(5)$ theory. Next let us bring Hilbert spaces into the game. We can take the basic properties of being up, down, red, green or blue, and treat them as basis vectors for ${\mathbb C}^5$. Let us call these vectors $u,d,r,g,b$. The exterior algebra $\Lambda {\mathbb C}^5$ has a basis given by wedge products of these 5 vectors. This exterior algebra is 32-dimensional, and it has a basis labelled by 5-bit strings. For example, the bit string $01100$ corresponds to the basis vector $d \wedge r$, while the bit string $10011$ corresponds to $u \wedge g \wedge b$.

Next we bring in representation theory. The group ${\rm SU}(5)$ has an obvious representation on ${\mathbb C}^5$. And since the operation of taking exterior algebras is functorial, this group also has a representation on $\Lambda {\mathbb C}^5$. In the ${\rm SU}(5)$ grand unified theory, this is the representation we use to describe a single generation of fermions and their antiparticles.

Just by our wording, though, we are picking out a splitting of ${\mathbb C}^5$ into ${\mathbb C}^2 \oplus {\mathbb C}^3$: the isospin and color parts, respectively. Choosing such a splitting of ${\mathbb C}^5$ picks out a subgroup of ${\rm SU}(5)$, the set of all group elements that preserve this splitting. This subgroup consists of block diagonal matrices with a $2
\times 2$ block and a $3 \times 3$ block, both unitary, such that the determinant of the whole matrix is 1. Let us denote this subgroup as ${\rm S}({\rm U}(2) \times {\rm U}(3))$.

Now for the miracle: the subgroup ${\rm S}({\rm U}(2) \times {\rm U}(3))$ is isomorphic to the Standard Model gauge group (at least modulo a finite subgroup). And, when we restrict the representation of ${\rm SU}(5)$ on $\Lambda
{\mathbb C}^5$ to ${\rm S}({\rm U}(2) \times {\rm U}(3))$, we get the Standard Model representation!

There are two great things about this. The first is that it gives a concise and mathematically elegant description of the Standard Model representation. The second is that the seemingly ad hoc hypercharges in the Standard Model *must be exactly what they are* for this description to work. So, physicists say the ${\rm SU}(5)$ theory explains the fractional charges of quarks: the fact that quark charges come in units $\frac{1}{3}$ the size of the electron charge pops right out of this theory.

With this foretaste of the fruits the ${\rm SU}(5)$ theory will bear, let us get to work and sow the seeds. Our work will have two parts. First we need to check that $${\rm S}({\rm U}(2) \times {\rm U}(3)) \cong{G_{\mbox{\rm SM}}}/N$$ where $N$ is some finite normal subgroup that acts trivially on $F \oplus F^*$. Then we need to check that indeed $$\Lambda{\mathbb C}^5 \cong F \oplus F^*$$ as representations of ${\rm S}({\rm U}(2) \times {\rm U}(3))$.

First, the group isomorphism. Naively, one might seek to build the ${\rm SU}(5)$ theory by including ${G_{\mbox{\rm SM}}}$ as a subgroup of ${\rm SU}(5)$. Can this be done? Clearly, we can include ${\rm SU}(2) \times {\rm SU}(3)$ as block diagonal matrices in ${\rm SU}(5)$: $$\begin{array}{ccc}
   {\rm SU}(2) \times {\rm SU}(3) &\to& {\rm SU}(5) \\
   (g, h) &\longmapsto& 
\left( 
\begin{array}{cc}
g & 0 \\
0 & h
\end{array}
\right).
\end{array}$$ but this is not enough, because ${G_{\mbox{\rm SM}}}$ also has that pesky factor of ${\rm U}(1)$, related to the hypercharge. How can we fit that in?

The first clue is that elements of ${\rm U}(1)$ must commute with the elements of ${\rm SU}(2) \times {\rm SU}(3)$. But the only elements of ${\rm SU}(5)$ that commute with everybody in the ${\rm SU}(2) \times {\rm SU}(3)$ subgroup are diagonal, since they must separately commute with ${\rm SU}(2) \times 1$ and $1 \times {\rm SU}(3)$, and the only elements doing so are diagonal. Moreover, they must be scalars on each block. So, they have to look like this: $$\left( 
\begin{array}{c c}
\alpha & 0 \\
0      & \beta
\end{array}
\right)$$ where $\alpha$ stands for the $2 \times 2$ identity matrix times the complex number $\alpha \in {\rm U}(1)$, and similarly for $\beta$ in the $3 \times 3$ block. For the above matrix to lie in ${\rm SU}(5)$, it must have determinant 1, so $\alpha^2 \beta^3 = 1$. This condition cuts the group of such matrices from ${\rm U}(1) \times {\rm U}(1)$ down to ${\rm U}(1)$. In fact, all such matrices are of the form $$\left( 
\begin{array}{c c}
\alpha^3 & 0 \\
0        & \alpha^{-2}
\end{array}
\right)$$ where $\alpha$ runs over ${\rm U}(1)$.

So if we throw in elements of this form, do we get ${\rm U}(1) \times
{\rm SU}(2) \times {\rm SU}(3)$? More precisely, does this map: $$\begin{array}{rccc}
  \phi \colon& {G_{\mbox{\rm SM}}}&\to& {\rm SU}(5) \\   
             & (\alpha, g, h) &\longmapsto& 
\left( 
\begin{array}{c c}
\alpha^{3}g & 0 \\
0           & \alpha^{-2}h
\end{array}
\right)
\end{array}$$ give an isomorphism between ${G_{\mbox{\rm SM}}}$ and ${\rm S}({\rm U}(2) \times {\rm U}(3))$? It is clearly a homomorphism. It clearly maps ${G_{\mbox{\rm SM}}}$ *into* the subgroup ${\rm S}({\rm U}(2) \times {\rm U}(3))$, and it is easy to check that it maps ${G_{\mbox{\rm SM}}}$ *onto* this subgroup. But is it one-to-one?

The answer is *no*: the map $\phi$ has a kernel, ${\mathbb Z}_6$. The kernel is the set of all elements of the form $$(\alpha, \alpha^{-3}, \alpha^2) \in {\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3)$$ and this is ${\mathbb Z}_6$, because scalar matrices $\alpha^{-3}$ and $\alpha^2$ live in ${\rm SU}(2)$ and ${\rm SU}(3)$, respectively, if and only if $\alpha$ is a sixth root of unity. So, all we get is $${G_{\mbox{\rm SM}}}/{\mathbb Z}_6 \cong {\rm S}({\rm U}(2) \times {\rm U}(3)) \hookrightarrow{\rm SU}(5).$$

This sets up a nerve-wracking test that the ${\rm SU}(5)$ theory must pass for it to have any chance of success. After all, not all representations of ${G_{\mbox{\rm SM}}}$ factor through ${G_{\mbox{\rm SM}}}/{\mathbb Z}_6$, but all those coming from representations of ${\rm SU}(5)$ must do so. A representation of ${G_{\mbox{\rm SM}}}$ will factor through ${G_{\mbox{\rm SM}}}/{\mathbb Z}_6$ only if the ${\mathbb Z}_6$ subgroup acts trivially.

In short: the ${\rm SU}(5)$ GUT is doomed unless ${\mathbb Z}_6$ acts trivially on every fermion. (And antifermion, but that amounts to the same thing.) For this to be true, some nontrivial relations between hypercharge, isospin and color must hold.

For example, consider the left-handed electron $$e^-_L \in {\mathbb C}_{-1} \otimes {\mathbb C}^2 \otimes {\mathbb C}.$$ For any sixth root of unity $\alpha$, we need $$(\alpha, \alpha^{-3}, \alpha^2) \in {\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3)$$ to act trivially on this particle. Let us see how it acts. Note that:

-   $\alpha \in {\rm U}(1)$ acts on ${\mathbb C}_{-1}$ as multiplication by $\alpha^{-3}$;

-   $\alpha^{-3} \in {\rm SU}(2)$ acts on ${\mathbb C}^2$ as multiplication by $\alpha^{-3}$;

-   $\alpha^2 \in {\rm SU}(3)$ acts trivially on ${\mathbb C}$.

So, we have $$(\alpha, \alpha^{-3}, \alpha^2) \cdot e^-_L = 
\alpha^{-3} \alpha^{-3} e^-_L = e^-_L .$$ The action is indeed trivial---precisely because $\alpha$ is a sixth root of unity.

Or, consider the right-handed $d$ quark: $$d_R \in {\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3.$$ How does $(\alpha, \alpha^{-3}, \alpha^2)$ act on this? We note:

-   $\alpha \in {\rm U}(1)$ acts on ${\mathbb C}_{-\frac{2}{3}}$ as multiplication by $\alpha^{-2}$;

-   $\alpha^{-3} \in {\rm SU}(2)$ acts trivially on the trivial representation ${\mathbb C}$;

-   $\alpha^2 \in {\rm SU}(3)$ acts on ${\mathbb C}^3$ as multiplication by $\alpha^2$.

So, we have $$(\alpha, \alpha^{-3}, \alpha^2) \cdot d_R 
= \alpha^{-2} \alpha^2 d_R = d_R .$$ Again, the action is trivial.

For ${\rm SU}(5)$ to work, though, ${\mathbb Z}_6$ has to act trivially on *every* fermion. There are 16 cases to check, and it is an awful lot to demand that hypercharge, the most erratic part of the Standard Model representation, satisfies 16 relations.

Or is it? In general, for a fermion with hypercharge $Y$, there are four distinct possibilities: 1em

::: center
  **Hypercharge relations**                                                                                                                          
  ---------------------------------------------------- --------------- ------------------------------------------------------------- --------------- ---------------------------
  Case                                                                                        Representation                                                  Relation
  Nontrivial ${\rm SU}(2)$, nontrivial ${\rm SU}(3)$    $\Rightarrow$   ${\mathbb C}_Y \otimes {\mathbb C}^2 \otimes {\mathbb C}^3$   $\Rightarrow$   $\alpha^{3Y - 3 + 2} = 1$
  Nontrivial ${\rm SU}(2)$, trivial ${\rm SU}(3)$       $\Rightarrow$    ${\mathbb C}_Y \otimes {\mathbb C}^2 \otimes {\mathbb C}$    $\Rightarrow$     $\alpha^{3Y - 3} = 1$
  Trivial ${\rm SU}(2)$, nontrivial ${\rm SU}(3)$       $\Rightarrow$    ${\mathbb C}_Y \otimes {\mathbb C}\otimes {\mathbb C}^3$     $\Rightarrow$     $\alpha^{3Y + 2} = 1$
  Trivial ${\rm SU}(2)$, trivial ${\rm SU}(3)$          $\Rightarrow$     ${\mathbb C}_Y \otimes {\mathbb C}\otimes {\mathbb C}$      $\Rightarrow$       $\alpha^{3Y} = 1$
:::

Better yet, say it like a physicist! 1em

::: center
  **Hypercharge relations**                                                                                                 
  --------------------------- --------------- ------------------------------------------------------------- --------------- ---------------------------
  Case                                                               Representation                                                  Relation
  Left-handed quark            $\Rightarrow$   ${\mathbb C}_Y \otimes {\mathbb C}^2 \otimes {\mathbb C}^3$   $\Rightarrow$   $\alpha^{3Y - 3 + 2} = 1$
  Left-handed lepton           $\Rightarrow$    ${\mathbb C}_Y \otimes {\mathbb C}^2 \otimes {\mathbb C}$    $\Rightarrow$     $\alpha^{3Y - 3} = 1$
  Right-handed quark           $\Rightarrow$    ${\mathbb C}_Y \otimes {\mathbb C}\otimes {\mathbb C}^3$     $\Rightarrow$     $\alpha^{3Y + 2} = 1$
  Right-handed lepton          $\Rightarrow$     ${\mathbb C}_Y \otimes {\mathbb C}\otimes {\mathbb C}$      $\Rightarrow$       $\alpha^{3Y} = 1$
:::

But $\alpha$ is sixth root of unity, so all this really says is that those exponents are multiples of six: 1em

::: center
  **Hypercharge relations**                   
  --------------------------- --------------- -------------------------------
  Case                                                   Relation
  Left-handed quark            $\Rightarrow$   $3Y - 3 + 2 \in 6{\mathbb Z}$
  Left-handed lepton           $\Rightarrow$     $3Y - 3 \in 6{\mathbb Z}$
  Right-handed quark           $\Rightarrow$     $3Y + 2 \in 6{\mathbb Z}$
  Right-handed lepton          $\Rightarrow$       $3Y \in 6{\mathbb Z}$
:::

Dividing by 3 and doing a little work, it is easy to see these are just saying: 1em

::: center
::: {#tab:hypercharge}
  **Hypercharge relations**   
  --------------------------- ------------------------------------
  Case                        Hypercharge
  Left-handed quark           $Y$ = even integer $+ \frac{1}{3}$
  Left-handed lepton          $Y$ = odd integer
  Right-handed quark          $Y$ = odd integer $+ \frac{1}{3}$
  Right-handed lepton         $Y$ = even integer

  : Hypercharge relations
:::
:::

Now it is easy to check that this indeed holds for every fermion in the standard model. ${\rm SU}(5)$ passes the test, not despite the bizarre pattern followed by hypercharges, but *because of it!*

By this analysis, we have shown that ${\mathbb Z}_6$ acts trivially on the Standard Model rep, so it is contained in the kernel of this rep. It is better than just a containment though: ${\mathbb Z}_6$ is the entire kernel. Because of this, we could say that ${G_{\mbox{\rm SM}}}/{\mathbb Z}_6$ is the 'true' gauge group of the Standard Model. And because we now know that $${G_{\mbox{\rm SM}}}/{\mathbb Z}_6 \cong{\rm S}({\rm U}(2) \times {\rm U}(3)) \hookrightarrow{\rm SU}(5),$$ it is almost as though this ${\mathbb Z}_6$ kernel, lurking inside ${G_{\mbox{\rm SM}}}$ this whole time, was a cryptic hint to try the ${\rm SU}(5)$ theory.

Of course, we still need to find a representation of ${\rm SU}(5)$ that extends the Standard Model representation. Luckily, there is a very beautiful choice that works: the exterior algebra $\Lambda{\mathbb C}^5$. Since ${\rm SU}(5)$ acts on ${\mathbb C}^5$, it has a representation on $\Lambda{\mathbb C}^5$. Our next goal is to check that pulling back this representation from ${\rm SU}(5)$ to ${G_{\mbox{\rm SM}}}$ using $\phi$, we obtain the Standard Model representation $F \oplus F^*.$

As we do this, we will see another fruit of the ${\rm SU}(5)$ theory ripen. The triviality of ${\mathbb Z}_6$ already imposed some structure on hypercharges, as outlined above in Table [1](#tab:hypercharge){reference-type="ref" reference="tab:hypercharge"}. As we fit the fermions into $\Lambda{\mathbb C}^5$, we will see this is no accident: the hypercharges have to be *exactly what they are* for the ${\rm SU}(5)$ theory to work.

To get started, our strategy will be to use the fact that, being representations of compact Lie groups, both the fermions $F \oplus
F^*$ and the exterior algebra $\Lambda{\mathbb C}^5$ are completely reducible, so they can be written as a direct sum of irreps. We will then match up these irreps one at a time.

The fermions are already written as a direct sum of irreps, so we need to work on $\Lambda{\mathbb C}^5$. Now, any element $g \in {\rm SU}(5)$ acts as an automorphism of the exterior algebra $\Lambda{\mathbb C}^5$: $$g(v \wedge w) = gv \wedge gw$$ where $v,w \in \Lambda{\mathbb C}^5$. Since we know how $g$ acts on the vectors in ${\mathbb C}^5$, and these generate $\Lambda{\mathbb C}^5$, this rule is enough to tell us how $g$ acts on all of $\Lambda{\mathbb C}^5$. This action respects grades in $\Lambda{\mathbb C}^5$, so each exterior power in $$\Lambda{\mathbb C}^5 \cong\Lambda^0 {\mathbb C}^5 \oplus \Lambda^1 {\mathbb C}^5 \oplus \Lambda^2 {\mathbb C}^5 \oplus \Lambda^3 {\mathbb C}^5 \oplus \Lambda^4 {\mathbb C}^5 \oplus \Lambda^5 {\mathbb C}^5$$ is a subrepresentation. In fact, these are all irreducible, so this is how $\Lambda{\mathbb C}^5$ breaks up into irreps of ${\rm SU}(5)$. Upon restriction to ${G_{\mbox{\rm SM}}}$, some of these summands break apart further into irreps of ${G_{\mbox{\rm SM}}}$.

Let us see how this works, starting with the easiest cases. $\Lambda^0
{\mathbb C}^5$ and $\Lambda^5 {\mathbb C}^5$ are both trivial irreps of ${G_{\mbox{\rm SM}}}$. There are two trivial irreps in the Standard Model representation, namely $\langle \nu_R \rangle$ and its dual $\langle \overline{\nu}_L \rangle$, where we use angle brackets to stand for the Hilbert space spanned by a vector or collection of vectors. So, we could select $\Lambda^0 {\mathbb C}^5 = \langle \overline{\nu}_L \rangle$ and $\Lambda^5
{\mathbb C}^5 = \langle \nu_R \rangle$, or vice versa. At this juncture, we have no reason to prefer one choice to the other.

Next let us chew on the next piece: the first exterior power, $\Lambda^1
{\mathbb C}^5$. We have $$\Lambda^1 {\mathbb C}^5 \cong{\mathbb C}^5$$ as vector spaces, and as representations of ${G_{\mbox{\rm SM}}}$. But what is ${\mathbb C}^5$ as a representation of ${G_{\mbox{\rm SM}}}$? The Standard Model gauge group acts on ${\mathbb C}^5$ via the map $$\phi \colon(\alpha, g, h) \longmapsto 
\left( 
\begin{array}{c c}
\alpha^{3}g & 0 \\
0 & \alpha^{-2}h
\end{array}
\right) .$$ Clearly, this action preserves the splitting into the 'isospin part' and the 'color part' of ${\mathbb C}^5$: $${\mathbb C}^5 \cong{\mathbb C}^2 \oplus {\mathbb C}^3 .$$ So, let us examine these two subrepresentations in turn:

-   The ${\mathbb C}^2$ part transforms in the hypercharge 1 rep of ${\rm U}(1)$: that is, $\alpha$ acts as multiplication by $\alpha^3$. It transforms according to the fundamental representation of ${\rm SU}(2)$, and the trivial representation of ${\rm SU}(3)$. This seems to describe a left-handed lepton with hypercharge 1.

-   The ${\mathbb C}^3$ part transforms in the hypercharge $-\frac{2}{3}$ rep of ${\rm U}(1)$: that is, $\alpha$ acts as multiplication by $\alpha^{-2}$. It transforms trivially under ${\rm SU}(2)$, and according to the fundamental representation of ${\rm SU}(3)$. Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"} shows that these are the features of a right-handed down quark.

In short, as a rep of ${G_{\mbox{\rm SM}}}$, we have $${\mathbb C}^5 \quad \cong\quad 
{\mathbb C}_1 \otimes {\mathbb C}^2 \otimes {\mathbb C}\quad \oplus 
\quad {\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3$$ and we have already guessed which particles these correspond to. The first summand looks like a left-handed lepton with hypercharge 1, while the second is a right-handed quark with hypercharge $-\frac{2}{3}$.

Now this is problematic, because another glance at Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"} reveals that there is no left-handed lepton with hypercharge 1. The only particles with hypercharge 1 are the right-handed antileptons, which span the representation $$\left\langle \! \begin{array}{c} e^+_R \\ \overline{\nu}_R \end{array} \! \right\rangle\cong{\mathbb C}_1 \otimes {\mathbb C}^{2*} \otimes {\mathbb C}.$$ But wait! ${\rm SU}(2)$ is unique among the ${\rm SU}(n)$'s in that its fundamental rep ${\mathbb C}^2$ is self-dual: $${\mathbb C}^2 \cong{\mathbb C}^{2*}.$$ This saves the day. As a rep of ${G_{\mbox{\rm SM}}}$, ${\mathbb C}^5$ becomes $${\mathbb C}^5 \quad \cong\quad
{\mathbb C}_1 \otimes {\mathbb C}^{2*} \otimes {\mathbb C}\quad \oplus \quad 
{\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3$$ so it describes the right-handed antileptons with hypercharge 1 and the right-handed quarks with hypercharge $-\frac{2}{3}$. In other words: $$\Lambda^1 {\mathbb C}^5 \cong{\mathbb C}^5 \cong\left\langle \! \begin{array}{c} e^+_R \\ \overline{\nu}_R \end{array} \! \right\rangle\oplus \langle d_R \rangle$$ where we have omitted the color label on $d_R$ to save space. Take heed of this: $\langle d_R \rangle$ is short for the vector space $\langle d^r_R, d^g_R, d^b_R \rangle$, and it is three-dimensional.

Now we can use our knowledge of the first exterior power to compute the second exterior power, by applying the formula $$\Lambda^2 (V \oplus W) \quad \cong\quad 
\Lambda^2 V \; \oplus \; (V \otimes W) \; \oplus \; \Lambda^2 W.$$

So, let us calculate! As reps of ${G_{\mbox{\rm SM}}}$ we have $$\Lambda^2 {\mathbb C}^5   \quad \cong\quad
\Lambda^2 ( {\mathbb C}_1 \otimes {\mathbb C}^2 \otimes {\mathbb C}\quad 
\oplus \quad {\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}^2 \otimes {\mathbb C}^3 )$$ $$\cong\quad
\Lambda^2 ( {\mathbb C}_1 \otimes {\mathbb C}^2 \otimes {\mathbb C}) \quad \oplus 
     \quad ({\mathbb C}_1 \otimes {\mathbb C}^2 \otimes {\mathbb C}) \otimes 
({\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3) \quad \oplus 
    \quad \Lambda^2 ( {\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3 ).$$

Consider the first summand, $\Lambda^2 ( {\mathbb C}_1 \otimes
{\mathbb C}^2 \otimes {\mathbb C})$. As a rep of ${\rm SU}(2)$ this space is just $\Lambda^2 {\mathbb C}^2$, which is the one-dimensional trivial rep, ${\mathbb C}$. As a rep of ${\rm SU}(3)$ it is also trivial. But as a rep of ${\rm U}(1)$, it is nontrivial. Inside it we are juxtaposing two particles with hypercharge 1. Hypercharges add, just like charges, so the composite particle, which consists of one particle *and* the other, has hypercharge 2. So, as a representation of the Standard Model gauge group we have $$\Lambda^2 ({\mathbb C}_1 \otimes {\mathbb C}^2 \otimes {\mathbb C}) \cong{\mathbb C}_2 \otimes {\mathbb C}\otimes {\mathbb C}.$$ Glancing at Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"} we see this matches the left-handed positron, $e^+_L$. Note that the hypercharges are becoming useful now, since they uniquely identify all the fermion and antifermion representations, except for neutrinos.

Next consider the second summand: $$({\mathbb C}_1 \otimes {\mathbb C}^2 \otimes {\mathbb C}) \otimes
({\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3) .$$ Again, we can add hypercharges, so this representation of ${G_{\mbox{\rm SM}}}$ is isomorphic to $${\mathbb C}_\frac{1}{3}\otimes {\mathbb C}^2 \otimes {\mathbb C}^3.$$ This is the space for left-handed quarks of hypercharge $\frac{1}{3}$, which from Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"} is: $$\left\langle \! \begin{array}{c} u_L \\ d_L \end{array} \! \right\rangle$$ where once again we have suppressed the label for colors.

Finally, the third summand in $\Lambda^2 {\mathbb C}^5$ is $$\Lambda^2 ( {\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3 ) .$$ This has isospin $-\frac{4}{3}$, so by Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"} it had better correspond to the left-handed antiup antiquark, which lives in the representation $${\mathbb C}_{-\frac{4}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^{3*}.$$ Let us check. The rep $\Lambda^2 ( {\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3 )$ is trivial under ${\rm SU}(2)$. As a rep of ${\rm SU}(3)$ it is the same as $\Lambda^2 {\mathbb C}^3$. But because ${\rm SU}(3)$ preserves the volume form on ${\mathbb C}^3$, taking Hodge duals gives an isomorphism $$\Lambda^p {\mathbb C}^3 \cong(\Lambda^{3 - p} {\mathbb C}^3)^*$$ so we have $$\Lambda^2 {\mathbb C}^3 \cong(\Lambda^1 {\mathbb C}^3)^* \cong{\mathbb C}^{3*}$$ which is just what we need to show

$$\Lambda^2 ( {\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}^3 ) \cong
 {\mathbb C}_{-\frac{4}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^{3*} \cong
\langle \overline{u}_L \rangle .$$

In summary, the following pieces of the Standard Model rep sit inside $\Lambda^2 {\mathbb C}^5$:

$$\Lambda^2 {\mathbb C}^5 \cong\langle e^+_L \rangle \oplus \left\langle \! \begin{array}{c} u_L \\ d_L \end{array} \! \right\rangle\oplus 
\langle \overline{u}_L \rangle$$

We are almost done. Because ${\rm SU}(5)$ preserves the canonical volume form on ${\mathbb C}^5$, taking Hodge duals gives an isomorphism between $$\Lambda^p {\mathbb C}^5 \cong(\Lambda^{5 - p} {\mathbb C}^5)^*$$ as representations of ${\rm SU}(5)$. Thus given our results so far: $$\begin{aligned}
\Lambda^0 {\mathbb C}^5 & \cong& \langle \overline{\nu}_L \rangle \\
\Lambda^1 {\mathbb C}^5 & \cong& \left\langle \! \begin{array}{c} e^+_R \\ \overline{\nu}_R \end{array} \! \right\rangle\oplus \langle d_R \rangle \\
\Lambda^2 {\mathbb C}^5 & \cong& \langle e^+_L \rangle \oplus \left\langle \! \begin{array}{c} u_L \\ d_L \end{array} \! \right\rangle\oplus 
\langle \overline{u}_L \rangle
\end{aligned}$$ we automatically get the antiparticles of these upon taking Hodge duals, $$\begin{aligned}
\Lambda^3 {\mathbb C}^5 & \cong& \langle e^-_R \rangle \oplus \left\langle \! \begin{array}{c} \overline{d}_R \\ \overline{u}_R \end{array} \! \right\rangle\oplus 
\langle u_R \rangle \\
\Lambda^4 {\mathbb C}^5 & \cong& \left\langle \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right\rangle\oplus \langle \overline{d}_L \rangle \\
\Lambda^5 {\mathbb C}^5 & \cong& \langle \nu_R \rangle.
\end{aligned}$$ So $\Lambda{\mathbb C}^5 \cong F \oplus F^*$, as desired.

How does all this look in terms of the promised binary code? Remember, a 5-bit code is short for a wedge product of basis vectors $u,d,r,g,b \in {\mathbb C}^5$. For example, 01101 corresponds to $d \wedge r \wedge b$. And now that we have found an isomorphism $\Lambda{\mathbb C}^5 \cong F \oplus F^*$, each of these wedge products corresponds to a fermion or antifermion. How does this correspondence go, exactly?

First consider the grade-one part $\Lambda^1 {\mathbb C}^5 \cong{\mathbb C}^2 \oplus {\mathbb C}^3$. This has basis vectors called $u,d,r,g,$ and $b$. We have seen that the subspace ${\mathbb C}^2$, spanned by $u$ and $d$, corresponds to $$\left\langle \! \begin{array}{c} e^+_R \\ \overline{\nu}_R \end{array} \! \right\rangle.$$ The top particle here has isospin up, while the bottom one has isospin down, so we must have $e^+_R = u$ and $\overline{\nu}_R = d$. Likewise, the subspace ${\mathbb C}^3$ spanned by $r,g$ and $b$ corresponds to $$\langle d_R \rangle = \langle d_R^r, d_R^g, d_R^b \rangle .$$ Thus we must have $d^c_R = c$, where $c$ runs over the colors $r,g,b$.

Next consider the grade-two part: $$\Lambda^2 {\mathbb C}^5  \cong\langle e^+_L \rangle \oplus \left\langle \! \begin{array}{c} u_L \\ d_L \end{array} \! \right\rangle\oplus 
\langle \overline{u}_L \rangle .$$ Here $e^+_L$ lives in the one-dimensional $\Lambda^2 {\mathbb C}^2$ rep of ${\rm SU}(2)$, which is spanned by the vector $u \wedge d$. Thus, $e^+_L = u \wedge d$. The left-handed quarks live in the ${\mathbb C}^2 \otimes {\mathbb C}^3$ rep of ${\rm SU}(2) \times {\rm SU}(3)$, which is spanned by vectors that consist of one isospin and one color. We must have $u^c_L = u \wedge c$ and $d^c_L = d \wedge c$, where again $c$ runs over all the colors $r,g,b$. And now for the tricky part: the $\overline{u}_L$ quarks live in the $\Lambda^2 {\mathbb C}^3$ rep of ${\rm SU}(3)$, but this is isomorphic to the fundamental representation of ${\rm SU}(3)$ on ${\mathbb C}^{3*}$, which is spanned by antired, antired and antiblue: $${\overline{r}}= g \wedge b , \qquad
   {\overline{g}}= b \wedge r , \qquad
   {\overline{b}}= r \wedge g.$$ These vectors form the basis of $\Lambda^2 {\mathbb C}^3$ that is dual to $r$, $g$, and $b$ under Hodge duality in $\Lambda{\mathbb C}^3$. So we must have $$u^{\overline{c}}_L = {\overline{c}}$$ where ${\overline{c}}$ can be any anticolor. Take heed of the fact that ${\overline{c}}$ is grade 2, even though it may look like grade 1.

To work out the other grades, note that Hodge duality corresponds to switching 0's and 1's in our binary code. For instance, the dual of 01101 is 10010: or written in terms of basis vectors, the dual of $d \wedge r \wedge b$ is $u \wedge g$. Thus given the binary codes for the first few exterior powers: 1em

::: center
  $\Lambda^0 {\mathbb C}^5$   $\Lambda^1 {\mathbb C}^5$   $\Lambda^2 {\mathbb C}^5$
  --------------------------- --------------------------- --------------------------------------------------
  $\overline{\nu}_L = 1$      $e^+_R = u$                 $e^+_L = u \wedge d$
                              $\overline{\nu}_R = d$      $u^c_L = u \wedge c$
                              $d^c_R = c$                 $d^c_L = d \wedge c$
                                                          $\overline{u}^{\overline{c}}_L = {\overline{c}}$
:::

1em taking Hodge duals gives the binary codes for the rest: 1em

::: center
  $\Lambda^3 {\mathbb C}^5$                                   $\Lambda^4 {\mathbb C}^4$                                            $\Lambda^5 {\mathbb C}^5$
  ----------------------------------------------------------- -------------------------------------------------------------------- -------------------------------------------------
  $e^-_R = r \wedge g \wedge b$                               $e^-_L = d \wedge r \wedge g \wedge b$                               $\nu_R = u \wedge d \wedge r \wedge g \wedge b$
  $\overline{u}^{\overline{c}}_R = d \wedge {\overline{c}}$   $\nu_L = u \wedge r \wedge g \wedge b$                               
  $\overline{d}^{\overline{c}}_R = u \wedge {\overline{c}}$   $\overline{d}^{\overline{c}}_L = u \wedge d \wedge {\overline{c}}$   
  $u^c_R = u \wedge d \wedge c$                                                                                                    
:::

1em Putting these together, we get the binary code for every particle and antiparticle in the first generation of fermions. To save space, let us omit the wedge product symbols: 1em

::: center
::: {#tab:su5code}
   **The Binary Code for ${\rm SU}(5)$**                                                                                                                                                                                          
  --------------------------------------- --------------------------- -------------------------------------------------- --------------------------------------------------- ---------------------------------------------------- ---------------------------
         $\Lambda^0 {\mathbb C}^5$         $\Lambda^1 {\mathbb C}^5$              $\Lambda^2 {\mathbb C}^5$                           $\Lambda^3 {\mathbb C}^5$                           $\Lambda^4 {\mathbb C}^4$                $\Lambda^5 {\mathbb C}^5$
                                                                                                                                                                                                                                  
          $\overline{\nu}_L = 1$                  $e^+_R = u$                            $e^+_L = ud$                                       $e^-_R = rgb$                                       $e^-_L = drgb$                          $\nu_R = udrgb$
                                                                                                                                                                                                                                  
                                            $\overline{\nu}_R = d$                       $u^c_L = uc$                     $\overline{u}^{\overline{c}}_R = d{\overline{c}}$                     $\nu_L = urgb$                    
                                                                                                                                                                                                                                  
                                                  $d^c_R = c$                            $d^c_L = dc$                     $\overline{d}^{\overline{c}}_R = u{\overline{c}}$   $\overline{d}^{\overline{c}}_L = ud{\overline{c}}$  
                                                                                                                                                                                                                                  
                                                                       $\overline{u}^{\overline{c}}_L = {\overline{c}}$                     $u^c_R = udc$                                                                         
                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                  

  : Binary code for first-generation fermions, where $c= r, g, b$ and ${\overline{c}}= gb, br, rg$
:::
:::

Now we can see a good, though not decisive, reason to choose $\Lambda^0 {\mathbb C}^5 \cong
\overline{\nu}_L$. With this choice, and not the other, we get left-handed particles in the even grades, and right-handed particles in the odd grades. We *choose* to have this pattern now, but later on we need it.

Table [2](#tab:su5code){reference-type="ref" reference="tab:su5code"} defines a linear isomorphism $f \colon F \oplus F^* \to
\Lambda{\mathbb C}^5$ in terms of the basis vectors, so the equations in this table are a bit of an exaggeration. When we write say, $e^+_R = u$, we really mean $f(e^+_R) = u$. This map $f$ is an isomorphism between representations of ${G_{\mbox{\rm SM}}}$. It tells us how these representations are the 'same'.

More precisely, we mean these representations are the same when we identify ${\rm S}({\rm U}(2) \times {\rm U}(3))$ with ${G_{\mbox{\rm SM}}}/{\mathbb Z}_6$ using the isomorphism induced by $\phi$. In general, we can think of a unitary representation as a Lie group homomorphism $$G \to {\rm U}(V)$$ where $V$ is a finite-dimensional Hilbert space and ${\rm U}(V)$ is the Lie group of unitary operators on $V$. In this section we have been comparing two unitary representations: an ugly, complicated representation of ${G_{\mbox{\rm SM}}}$: $${G_{\mbox{\rm SM}}}\to {\rm U}(F \oplus F^*)$$ and a nice, beautiful representation of ${\rm SU}(5)$: $${\rm SU}(5) \to {\rm U}(\Lambda{\mathbb C}^5).$$ We built a homomorphism $$\phi \colon{G_{\mbox{\rm SM}}}\to {\rm SU}(5),$$ so it is natural to wonder if is there a fourth homomorphism $${\rm U}(F \oplus F^*) \to {\rm U}(\Lambda{\mathbb C}^5)$$ such that this square: $$\xymatrix{
{G_{\mbox{\rm SM}}}\ar[r]^\phi \ar[d] & {\rm SU}(5) \ar[d] \\
{\rm U}(F \oplus F^*) \ar[r] & {\rm U}(\Lambda{\mathbb C}^5)
}$$ commutes.

Indeed, we just showed this! We have seen that there exists a unitary operator from the Standard Model rep to $\Lambda{\mathbb C}^5$, say $$f \colon F \oplus F^* \stackrel{\sim}{\to} \Lambda{\mathbb C}^5 ,$$ such that the induced isomorphism of the unitary groups, $${\rm U}(f) \colon{\rm U}(F \oplus F^*) \stackrel{\sim}{\to} {\rm U}(\Lambda{\mathbb C}^5),$$ makes the above square commute. So, let us summarize this result as a theorem:

::: thm
[]{#thm:su(5) label="thm:su(5)"} The following square commutes: $$\xymatrix{
    {G_{\mbox{\rm SM}}}\ar[r]^\phi \ar[d] & {\rm SU}(5) \ar[d] \\
    {\rm U}(F \oplus F^*) \ar[r]^-{{\rm U}(f)} & {\rm U}(\Lambda{\mathbb C}^5)
    }$$ where the left vertical arrow is the Standard Model representation and the right one is the natural representation of ${\rm SU}(5)$ on the exterior algebra of ${\mathbb C}^5$.
:::
