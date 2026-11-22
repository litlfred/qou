---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-017-33-the-patisalam-model
section_title: "The Pati–Salam Model"
section_number: 3.3
pages: 48-55
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.997
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:g(2,2,4) label="sec:g(2,2,4)"}

Next we turn to a unified theory that is not so 'grand': its gauge group is not a simple Lie group, as it was for the ${\rm SU}(5)$ and ${\rm Spin}(10)$ theories. This theory is called the Pati--Salam model, after its inventors [@PatiSalam:model]; it has gauge group ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$, which is merely semisimple.

We might imagine the ${\rm SU}(5)$ theory as an answer to this question:

> Why are the hypercharges in the Standard Model what they are?

The answer it provides is something like this:

> Because ${\rm SU}(5)$ is the actual gauge group of the world, acting on the representation $\Lambda{\mathbb C}^5$.

But there are other intriguing patterns in the Standard Model that ${\rm SU}(5)$ does *not* explain---and these lead us in different directions.

First, there is a strange similarity between quarks and leptons. Each generation of fermions in the Standard Model has two quarks and two leptons. For example, in the first generation we have the quarks $u$ and $d$, and the leptons $\nu$ and $e^-$. The quarks come in three 'colors': this is a picturesque way of saying that they transform in the fundamental representation of ${\rm SU}(3)$ on ${\mathbb C}^3$. The leptons, on the other hand, are 'white': they transform in the trivial representation of ${\rm SU}(3)$ on ${\mathbb C}$. 1em

::: center
  **Representations of ${\rm SU}(3)$**   
  -------------------------------------- -----------------
  Particle                                Representation
  Quark                                   ${\mathbb C}^3$
  Lepton                                   ${\mathbb C}$
:::

1em Could the lepton secretly be a fourth color of quark? Maybe it could in a theory where the ${\rm SU}(3)$ color symmetry of the Standard Model is extended to ${\rm SU}(4)$. Of course this larger symmetry would need to be broken to explain the very real *difference* between leptons and quarks.

Second, there is a strange difference between left- and right-handed fermions. The left-handed ones participate in the weak force governed by ${\rm SU}(2)$, while the right-handed ones do not. Mathematically speaking, the left-handed ones live in a nontrivial representation of ${\rm SU}(2)$, while the right-handed ones live in a trivial one. The nontrivial one is ${\mathbb C}^2$, while the trivial one is ${\mathbb C}\oplus {\mathbb C}$: 1em

::: center
  **Representations of ${\rm SU}(2)$**   
  -------------------------------------- ---------------------------------
  Particle                                        Representation
  Left-handed fermion                             ${\mathbb C}^2$
  Right-handed fermion                    ${\mathbb C}\oplus {\mathbb C}$
:::

1em But there is a suspicious similarity between ${\mathbb C}^2$ and ${\mathbb C}\oplus {\mathbb C}$. Could there be another copy of ${\rm SU}(2)$ that acts on the right-handed particles? Again, this 'right-handed' ${\rm SU}(2)$ would need to be broken, to explain why we do not see a 'right-handed' version of the weak force that acts on right-handed particles.

Following Pati and Salam, let us try to sculpt a theory that makes these ideas precise. In the last two sections, we saw some of the ingredients we need to make a grand unified theory: we need to extend the symmetry group ${G_{\mbox{\rm SM}}}$ to a larger group $G$ using an inclusion $${G_{\mbox{\rm SM}}}\hookrightarrow G$$ (up to some discrete kernel), and we need a representation $V$ of $G$ which reduces to the Standard Model representation when restricted to ${G_{\mbox{\rm SM}}}$: $$F \oplus F^* \cong V.$$ We can put all these ingredients together into a diagram $$\xymatrix{
    {G_{\mbox{\rm SM}}}\ar[r] \ar[d] & G \ar[d] \\
    {\rm U}(F \oplus F^*) \ar[r]^-\sim    & {\rm U}(V)   \\
}$$ which commutes only when our $G$ theory works out.

We now use the same methods to chip away at our current challenge. We asked if leptons correspond to a fourth color. We already know that every quark comes in three colors, $r$, $g$, and $b$, which form a basis for the vector space ${\mathbb C}^3$. This is the fundamental representation of ${\rm SU}(3)$, the color symmetry group of the Standard Model. If leptons correspond to a fourth color, say 'white', then we should use the colors $r$, $g$, $b$ and $w$, as a basis for the vector space ${\mathbb C}^4$. This is the fundamental representation of ${\rm SU}(4)$, so let us take that group to describe color symmetries in our new GUT.

Now ${\rm SU}(3)$ has an obvious inclusion into ${\rm SU}(4)$, using block diagonal matrices: $$g \mapsto 
\left(
\begin{array}{cc}
    g & 0 \\
    0 & 1
\end{array}
\right)$$ When restricted to this subgroup, the fundamental representation ${\mathbb C}^4$ breaks into a direct sum of irreps: $${\mathbb C}^4 \cong{\mathbb C}^3 \oplus {\mathbb C}.$$ These are precisely the irreps of ${\rm SU}(3)$ that describe quarks and leptons. For antiquarks and antileptons we can use $${\mathbb C}^{4*} \cong{\mathbb C}^{3*} \oplus {\mathbb C}.$$ It looks like we are on the right track.

We can do even better if we *start* with the splitting $${\mathbb C}^4 \cong{\mathbb C}^3 \oplus {\mathbb C}.$$ Remember that when we studied ${\rm SU}(5)$, the splitting $${\mathbb C}^5 \cong{\mathbb C}^2 \oplus {\mathbb C}^3$$ had the remarkable effect of introducing ${\rm U}(1)$, and thus hypercharge, into ${\rm SU}(5)$ theory. This was because the subgroup of ${\rm SU}(5)$ that preserves this splitting is larger than ${\rm SU}(2) \times
{\rm SU}(3)$, roughly by a factor of ${\rm U}(1)$: $$({\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3)) / {\mathbb Z}_6 \cong{\rm S}({\rm U}(2) \times {\rm U}(3))$$ It was this factor of ${\rm U}(1)$ that made ${\rm SU}(5)$ theory so fruitful.

So, if we choose a splitting ${\mathbb C}^4 \cong{\mathbb C}^3 \oplus {\mathbb C},$ we should again look at the subgroup that preserves this splitting. Namely: $${\rm S}({\rm U}(3) \times {\rm U}(1)) \subseteq {\rm SU}(4) .$$ Just as in the ${\rm SU}(5)$ case, this group is bigger than ${\rm SU}(3) \times
{\rm SU}(1)$, roughly by a factor of ${\rm U}(1)$. And again, this factor of ${\rm U}(1)$ is related to hypercharge!

This works very much as it did for ${\rm SU}(5)$. We want a map $${\rm U}(1) \times {\rm SU}(3) \to {\rm SU}(4)$$ and we already have one that works for the ${\rm SU}(3)$ part: $$\begin{array}{ccc}
 {\rm SU}(3) &\to & {\rm SU}(4) \\
 h &\mapsto & 
\left(
\begin{array}{cc}
    h & 0 \\
    0 & 1
\end{array}
\right)
\end{array}$$ So, we just need to include a factor of ${\rm U}(1)$ that commutes with everything in the ${\rm SU}(3)$ subgroup. Elements of ${\rm SU}(4)$ that do this are of the form $$\left( 
\begin{array}{c c}
\alpha & 0 \\
0 & \beta
\end{array}
\right)$$ where $\alpha$ stands for the $3 \times 3$ identity matrix times the complex number $\alpha \in {\rm U}(1)$, and similarly for $\beta$ in the $1 \times 1$ block. For the above matrix to lie in ${\rm SU}(4)$, it must have determinant 1, so $\alpha^3 \beta = 1$. Thus we must include ${\rm U}(1)$ using matrices of this form: $$\left( 
\begin{array}{c c}
\alpha & 0 \\
0 & \alpha^{-3}
\end{array}
\right).$$ This gives our map: $$\begin{array}{ccc}
 {\rm U}(1) \times {\rm SU}(3) &\to& {\rm SU}(4)  \\
( \alpha, h) &\mapsto &
\left( 
\begin{array}{c c}
\alpha h & 0 \\
0 & \alpha^{-3}
\end{array}
\right) .
\end{array}$$

If we let ${\rm U}(1) \times {\rm SU}(3)$ act on ${\mathbb C}^4 \cong{\mathbb C}^3 \oplus {\mathbb C}$ via this map, the 'quark part' ${\mathbb C}^3$ transforms as though it has hypercharge $\frac{1}{3}$: that is, it gets multiplied by a factor of $\alpha$. Meanwhile, the 'lepton part' ${\mathbb C}$ transforms as though it has hypercharge $-1$, getting multiplied by a factor of $\alpha^{-3}$. So, as a representation of ${\rm U}(1) \times {\rm SU}(3)$, we have $${\mathbb C}^4 \quad \cong\quad
{\mathbb C}_{\frac{1}{3}} \otimes {\mathbb C}^3 \quad \oplus \quad {\mathbb C}_{-1} \otimes {\mathbb C}.$$ A peek at Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"} reveals something nice. This is exactly how the left-handed quarks and leptons in the Standard Model transform under ${\rm U}(1) \times {\rm SU}(3)$!

The right-handed leptons do not work this way. That is a problem we need to address. But this brings us to our second question, which was about the strange difference between left- and right-handed particles.

Remember that in the Standard Model, the left-handed particles live in the fundamental rep of ${\rm SU}(2)$ on ${\mathbb C}^2$, while the right-handed ones live in the trivial rep on ${\mathbb C}\oplus {\mathbb C}$. Physicists write this by grouping left-handed particles into 'doublets', while leaving the right-handed particles as 'singlets': $$\left( \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right)\quad \quad 
\begin{array}{c}
    \nu_R \\
    e^-_R 
\end{array}.$$ But there is a suspicious similarity between ${\mathbb C}^2$ and ${\mathbb C}\oplus {\mathbb C}$. Could there be another copy of ${\rm SU}(2)$ that acts on the right-handed particles? Physically speaking, this would mean that the left- and right-handed particles both form doublets: $$\left( \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right)\quad \quad 
\left( \!
\begin{array}{c}
    \nu_R \\
    e^-_R
\end{array}
\! \right)$$ but under the actions of different ${\rm SU}(2)$'s. Mathematically, this would amount to extending the representations of the 'left-handed' ${\rm SU}(2)$: $${\mathbb C}^2 \quad \quad {\mathbb C}\oplus {\mathbb C}$$ to representations of ${\rm SU}(2) \times {\rm SU}(2)$: $${\mathbb C}^2 \otimes {\mathbb C}\quad \quad {\mathbb C}\otimes {\mathbb C}^2$$ where the first copy of ${\rm SU}(2)$ acts on the first factor in these tensor products, while the second copy acts on the second factor. The first copy of ${\rm SU}(2)$ is the 'left-handed' one familiar from the Standard Model. The second copy is a new 'right-handed' one.

If we restrict these representations to the 'left-handed' ${\rm SU}(2)$ subgroup, we obtain: $$\begin{aligned}
    {\mathbb C}^2 \otimes {\mathbb C}& \cong& {\mathbb C}^2 \\ 
    {\mathbb C}\otimes {\mathbb C}^2 & \cong& {\mathbb C}\oplus {\mathbb C}.
\end{aligned}$$ These are exactly the representations of ${\rm SU}(2)$ that appear in the Standard Model. It looks like we are on the right track!

Now let us try to combine these ideas into a theory with symmetry group ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$. We have seen that letting ${\rm SU}(4)$ act on ${\mathbb C}^4$ is a good way to unify our treatment of color for all the left-handed fermions. Similarly, the dual representation on ${\mathbb C}^{4*}$ is good for their antiparticles. So, we will tackle color by letting ${\rm SU}(4)$ act on the direct sum ${\mathbb C}^4 \oplus {\mathbb C}^{4*}$. This space is 8-dimensional. We have also seen that letting ${\rm SU}(2) \times {\rm SU}(2)$ act on ${\mathbb C}^2 \otimes {\mathbb C}\oplus {\mathbb C}\otimes {\mathbb C}^2$ is a good way to unify our treatment of isospin for left- and right-handed fermions. This space is 4-dimensional.

Since $8 \times 4 = 32$, and the Standard Model representation is 32-dimensional, let us take the tensor product $$V =   \big(({\mathbb C}^2 \otimes {\mathbb C}) \; \oplus \; ({\mathbb C}\otimes {\mathbb C}^2)\big)
\; \otimes \; \big({\mathbb C}^4 \; \oplus \; {\mathbb C}^{4*}\big).$$ This becomes a representation of ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$, which we call the **Pati--Salam representation**. To obtain a theory that extends the Standard Model, we also need a way to map ${G_{\mbox{\rm SM}}}$ to ${\rm SU}(2) \times {\rm SU}(2) \times 
{\rm SU}(4)$, such that pulling back $V$ to a representation of ${G_{\mbox{\rm SM}}}$ gives the Standard model representation.

How can we map ${G_{\mbox{\rm SM}}}$ to ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$? There are several possibilities. Our work so far suggests this option: $$\begin{array}{ccl}
{\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3) &\to& {\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \\
  (\alpha, g, h)  &\mapsto&  
\left( g, \; 1, \;
\left(
\begin{array}{c c}
    \alpha h & 0 \\
    0 & \alpha^{-3}
\end{array}
\right) 
\right)
\end{array}$$

Let us see what this gives. The Pati--Salam representation of ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$ is a direct sum of four irreducibles: $$V \quad \cong\quad 
{\mathbb C}^2 \otimes {\mathbb C}\otimes {\mathbb C}^4 \quad \oplus \quad
{\mathbb C}\otimes {\mathbb C}^2 \otimes {\mathbb C}^4 \quad \oplus \quad
{\mathbb C}^2 \otimes {\mathbb C}\otimes {\mathbb C}^{4*} \quad \oplus \quad
{\mathbb C}\otimes {\mathbb C}^2 \otimes {\mathbb C}^{4*}.$$ We hope the first two will describe left- and right-handed fermions, so let us give them names that suggest this: $$F_L = {\mathbb C}^2 \otimes {\mathbb C}\otimes {\mathbb C}^4,$$ $$F_R = {\mathbb C}\otimes {\mathbb C}^2 \otimes {\mathbb C}^4 .$$ The other two are the duals of the first two, since the 2-dimensional irrep of ${\rm SU}(2)$ is its own dual: $$F_L^* = {\mathbb C}^2 \otimes {\mathbb C}\otimes {\mathbb C}^{4*},$$ $$F_R^* = {\mathbb C}\otimes {\mathbb C}^2 \otimes {\mathbb C}^{4*} .$$

Given our chosen map from ${G_{\mbox{\rm SM}}}$ to ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$, we can work out which representations of the ${G_{\mbox{\rm SM}}}$ these four spaces give. For example, consider $F_L$. We have already seen that under our chosen map, $${\mathbb C}^4 \quad \cong\quad
{\mathbb C}_{\frac{1}{3}} \otimes {\mathbb C}^3 \quad \oplus \quad {\mathbb C}_{-1} \otimes {\mathbb C}$$ as representations of ${\rm U}(1) \times {\rm SU}(3)$, while $${\mathbb C}^2 \otimes {\mathbb C}\cong{\mathbb C}^2$$ as representations of the left-handed ${\rm SU}(2)$. So, as representations of ${G_{\mbox{\rm SM}}}$ we have $$F_L \quad \cong
\quad {\mathbb C}_{\frac{1}{3}} \otimes {\mathbb C}^2 \otimes {\mathbb C}^3  \quad \oplus 
\quad {\mathbb C}_{-1} \otimes {\mathbb C}^2 \otimes {\mathbb C}.$$ Table [\[tab:smrep\]](#tab:smrep){reference-type="ref" reference="tab:smrep"} shows that these indeed match the left-handed fermions.

If we go ahead and do the other four cases, we see that everything works *except for the hypercharges of the right-handed particles*---and their antiparticles. Here we just show results for the particles:

::: center
::: tabular
ccc **The Pati--Salam Model --- First Try**\
Particle & Hypercharge: predicted & Hypercharge: actual\
\
$\left( \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right)$ & $-1$ & $-1$\
\
$\left( \! \begin{array}{c} u_L \\ d_L \end{array} \! \right)$ & $\frac{1}{3}$ & $\frac{1}{3}$\
\
$\nu_R$ & $-1$ & $0$\
\
$e^-_R$ & $-1$ & $-2$\
\
$u_R$ & $\frac{1}{3}$ & $\frac{4}{3}$\
\
$d_R$ & $\frac{1}{3}$ & $-\frac{2}{3}$\
\
:::
:::

The problem is that the right-handed particles are getting the same hypercharges as their left-handed brethren. To fix this problem, we need a more clever map from ${G_{\mbox{\rm SM}}}$ to ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$. This map must behave differently on the ${\rm U}(1)$ factor of ${G_{\mbox{\rm SM}}}$, so the hypercharges come out differently. And it must take advantage of the right-handed copy of ${\rm SU}(2)$, which acts nontrivially only on the right-handed particles. For example, we can try this map: $$\begin{array}{ccc}
{\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3) &\to& {\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \\
  (\alpha, g, h)  &\mapsto&  
\left( g, \;
\left(
\begin{array}{c c}
    \alpha^k & 0 \\
    0 & \alpha^{-k}
\end{array}
\right), \;
\left(
\begin{array}{c c}
    \alpha h & 0 \\
    0 & \alpha^{-3}
\end{array}
\right) 
\right)
\end{array}$$ for any integer $k$. This will not affect the above table except for the hypercharges of right-handed particles. It will add $k/3$ to the hypercharges of the 'up' particles in right-handed doublets ($\nu_R$ and $u_R$), and subtract $k/3$ from the 'down' ones ($e^-_R$ and $d_R$). So, we obtain these results:

::: center
                **The Pati--Salam Model --- Second Try**                                            
  -------------------------------------------------------------------- ---------------------------- ---------------------
                                Particle                                  Hypercharge: predicted     Hypercharge: actual
                                                                                                    
   $\left( \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right)$              $-1$                     $-1$
                                                                                                    
     $\left( \! \begin{array}{c} u_L \\ d_L \end{array} \! \right)$           $\frac{1}{3}$             $\frac{1}{3}$
                                                                                                    
                                $\nu_R$                                     $-1 + \frac{k}{3}$               $0$
                                                                                                    
                                $e^-_R$                                     $-1 - \frac{k}{3}$              $-2$
                                                                                                    
                                 $u_R$                                  $\frac{1}{3}+ \frac{k}{3}$      $\frac{4}{3}$
                                                                                                    
                                 $d_R$                                  $\frac{1}{3}- \frac{k}{3}$     $-\frac{2}{3}$
                                                                                                    
:::

Miraculously, all the hypercharges match if we choose $k = 3$. So, let us use this map: $$\begin{array}{ccc}
\beta \colon{\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3) 
&\to& {\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \\  \\
  (\alpha, g, h)  &\mapsto&  
\left( g, \;
\left(
\begin{array}{c c}
    \alpha^3 & 0 \\
    0 & \alpha^{-3}
\end{array}
\right), \;
\left(
\begin{array}{c c}
    \alpha h & 0 \\
    0 & \alpha^{-3}
\end{array}
\right) 
\right).
\end{array}$$ When we take the Pati--Salam representation of ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$ and pull it back along this map $\beta$, we obtain the Standard Model representation. As in Section [\[sec:su(5)\]](#sec:su(5)){reference-type="ref" reference="sec:su(5)"}, we use complete reducibility to see this, but we can be more concrete. We saw in Table [\[tab:su5code\]](#tab:su5code){reference-type="ref" reference="tab:su5code"} how we can specify the intertwining map precisely by using a specific basis, which for $\Lambda {\mathbb C}^5$ results in the binary code.

Similarly, we can create a kind of 'Pati--Salam code' to specify an isomorphism of Hilbert spaces $$\ell \colon F
\oplus F^* \to \big(({\mathbb C}^2 \otimes {\mathbb C}) \; \oplus \; ({\mathbb C}\otimes {\mathbb C}^2)\big) \;
\otimes \; \big({\mathbb C}^4 \; \oplus \; {\mathbb C}^{4*}\big),$$ and doing this provides a nice summary of the ideas behind the Pati--Salam model. We take the space ${\mathbb C}^2 \otimes {\mathbb C}$ to be spanned by $u_L$ and $d_L$, the **left-isospin up** and **left-isospin down** states. Similarly, the space ${\mathbb C}\otimes
{\mathbb C}^2$ has basis $u_R$ and $d_R$, called **right-isospin up** and **right-isospin down**. Take care not to confuse these with the similarly named quarks. These have no color, and only correspond to isospin.

The color comes from ${\mathbb C}^4$ of course, which we already decreed to be spanned by $r$, $g$, $b$ and $w$. For antiparticles, we also require anticolors, which we take to be the dual basis ${\overline{r}}$, ${\overline{g}}$, ${\overline{b}}$ and ${\overline{w}}$, spanning ${\mathbb C}^{4*}$.

It is now easy, with our knowledge of how the Pati--Salam model is to work, to construct this code. Naturally, the left-handed quark doublet corresponds to the left-isospin up and down states, which come in all three colors $c = r,g,b$: $$u^c_L = u_L \otimes c \quad \quad d^c_L = d_L \otimes c.$$ The corresponding doublet of left-handed leptons is just the 'white' version of this: $$\nu_L = u_L \otimes w \quad \quad e^-_L = d_L \otimes w .$$ The right-handed fermions are the same, but with $R$'s instead of $L$'s. Thus we get the Pati--Salam code for the fermions: 1em

::: center
            $F_L$                     $F_R$
  ------------------------- -------------------------
   $\nu_L = u_L \otimes w$   $\nu_R = u_R \otimes w$
   $e^-_L = d_L \otimes w$   $e^-_R = d_R \otimes w$
   $u^c_L = u_L \otimes c$   $u^c_R = u_R \otimes c$
   $d^c_L = d_L \otimes c$   $d^c_R = d_R \otimes c$
:::

1em The result is very similar for the antifermions in $F^*_L$ and $F^*_R$, but watch out: taking antiparticles *swaps up and down*, and also *swaps left and right*, so the particles in $F^*_L$ are right-handed, despite the subscript $L$, while those in $F^*_R$ are left-handed. This is because it is the right-handed antiparticles that feel the weak force, which in terms of representation theory means they are nontrivial under the left ${\rm SU}(2)$. So, the Pati--Salam code for the antifermions is this: 1em

::: center
                             $F^*_L$                                                        $F^*_R$
  -------------------------------------------------------------- --------------------------------------------------------------
           $e^+_R         = u_L \otimes {\overline{w}}$                   $e^+_L         = u_R \otimes {\overline{w}}$
       $\overline{\nu}_R      = d_L \otimes {\overline{w}}$           $\overline{\nu}_L      = d_R \otimes {\overline{w}}$
   $\overline{d}^{\overline{c}}_R = u_L \otimes {\overline{c}}$   $\overline{d}^{\overline{c}}_L = u_R \otimes {\overline{c}}$
   $\overline{u}^{\overline{c}}_R = d_L \otimes {\overline{c}}$   $\overline{u}^{\overline{c}}_L = d_R \otimes {\overline{c}}$
:::

1em Putting these together we get the full Pati--Salam code: 1em

::: center
::: {#tab:pscode1}
   **The Pati--Salam Code**                                                                                           
  -------------------------- ------------------------- -------------------------------------------------------------- --------------------------------------------------------------
            $F_L$                      $F_R$                                      $F^*_L$                                                        $F^*_R$
   $\nu_L = u_L \otimes w$    $\nu_R = u_R \otimes w$           $e^+_R         = u_L \otimes {\overline{w}}$                   $e^+_L         = u_R \otimes {\overline{w}}$
   $e^-_L = d_L \otimes w$    $e^-_R = d_R \otimes w$       $\overline{\nu}_R      = d_L \otimes {\overline{w}}$           $\overline{\nu}_L      = d_R \otimes {\overline{w}}$
   $u^c_L = u_L \otimes c$    $u^c_R = u_R \otimes c$   $\overline{d}^{\overline{c}}_R = u_L \otimes {\overline{c}}$   $\overline{d}^{\overline{c}}_L = u_R \otimes {\overline{c}}$
   $d^c_L = d_L \otimes c$    $d^c_R = d_R \otimes c$   $\overline{u}^{\overline{c}}_R = d_L \otimes {\overline{c}}$   $\overline{u}^{\overline{c}}_L = d_R \otimes {\overline{c}}$

  : Pati--Salam code for first-generation fermions, where $c = r, g, b$ and ${\overline{c}}= {\overline{r}}, {\overline{b}}, {\overline{g}}$.
:::
:::

-1em

This table defines an isomorphism of Hilbert spaces $$\ell \colon F
\oplus F^* \to \big(({\mathbb C}^2 \otimes {\mathbb C}) \; \oplus \; ({\mathbb C}\otimes {\mathbb C}^2)\big) \;
\otimes \; \big({\mathbb C}^4 \; \oplus \; {\mathbb C}^{4*}\big)$$ so where it says, for example, $\nu_L = u_L \otimes w$, that is just short for $\ell(\nu_L) = u_L \otimes w$. This map $\ell$ is also an isomorphism between representations of ${G_{\mbox{\rm SM}}}$. It tells us how these representations are the 'same', just as the map $h$ did for $F \oplus F^*$ and $\Lambda{\mathbb C}^5$ at the end of Section [\[sec:su(5)\]](#sec:su(5)){reference-type="ref" reference="sec:su(5)"}.

As with ${\rm SU}(5)$ and ${\rm Spin}(10)$, we can summarize all the results of this section in a commutative square:

::: thm
[]{#thm:Pati--Salam label="thm:Pati--Salam"} The following square commutes: $$\xymatrix{
{G_{\mbox{\rm SM}}}\ar[r]^-{\beta} \ar[d]  & {\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4) \ar[d] \\
{\rm U}( F \oplus F^* ) \ar[r]^-{U(\ell)} & 
{\rm U}\left(\big(({\mathbb C}^2 \otimes {\mathbb C}) \oplus ({\mathbb C}\otimes {\mathbb C}^2)\big)
\otimes \big({\mathbb C}^4 \oplus {\mathbb C}^{4*}\big)\right) \\
}$$ where the left vertical arrow is the Standard Model representation and the right one is the Pati--Salam representation.
:::

The Pati--Salam representation and especially the homomorphism $\beta$ look less natural than the representation of ${\rm SU}(5)$ on $\Lambda {\mathbb C}^5$ and the homomorphism $\phi \colon{G_{\mbox{\rm SM}}}\to {\rm SU}(5)$. But appearances can be deceiving: in the next section we shall see a more elegant way to describe them.
