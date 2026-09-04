---
doc_id: arxiv-2103.00651v1
doc_title: "On Concentration Inequalities for Vector-Valued Lipschit z Functions Dimitrios Katselis katselis@illinois.edu"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2103.00651v1.pdf
source_sha256: c5505d3e4891168e
doc_brief: "On Concentration Inequalities for Vector-Valued Lipschit z Functions Dimitrios Katselis katselis@illinois.edu — We derive two upper bounds for the probability of deviation of a vect or-valued"
---
In many statistical settings, vector-valued estimators na turally arise and determining their
statistical rates is essential. As an example, assume that X = ( X1, . . . , Xn) corresponds
to a random sample drawn from a product measure ν⊗n
θ , denoted by X ∼ ν⊗n
θ , where θ
is a parameter vector taking values in a compact set Θ ⊂ Rk with a ﬁxed dimension k
independent of n. In this case, ˆθn = f (X) is a candidate vector-valued estimator of θ,
where f is a measurable function with respect to X. In such settings, we are interested in
knowing how close f (X) is to its expectation Eν[f (X)]. Concentration inequalities for f (X)
when the deviation from Eν[f (X)] is measured in terms of a metric, often norm-induced,
are important.
The derivation of concentration bounds relies on imposing s moothness conditions on f ,
which guarantee that f is not very sensitive to any particular coordinate variable Boucheron et al.
(2013); Raginsky and Sason (2014); Van Handel (2016). This s ensitivity is quantiﬁed either
locally via gradients or globally via Lipschitz properties of f . Marton introduced the trans-
portation method to establish concentration of measure for product measures and Markov
chains Marton (1986, 1996) by showing that transportation c ost inequalities can be used
to deduce concentration. In Bobkov and G¨ otze (1999), Bobko v and G¨ otze extended Mar-
ton’s argument into an equivalence by showing that Wasserstein distances and relative
entropies are comparable only when the moment-generating f unctions of real-valued Lip-
schitz functions deﬁned with respect to the underlying metr ic can be controlled and vice
1
versa. The connection between moment-generating function s and the two aforementioned
indices of closeness of probability measures is establishe d via the Gibbs variational principle
Van Handel (2016),Dembo and Zeitouni (1998) or alternative ly, via the Donsker-Varadhan
lemma Rezakhanlou (2015).
A key example in showing the connection between concentrati on of measure and Lip-
schitz functions is McDiarmid’s or bounded-diﬀerence inequality McDiarmid (1997), tradi-
tionally viewed as a result of the martingale approach in establishing concentration Boucheron et al.
(2013); Raginsky and Sason (2014); Van Handel (2016). Let ea ch Xi take values in a mea-
surable space Xi and equip the product space X = X1 × · × Xn with the weighted Hamming
metric dc(x, y) = ∑ n
i=1 ci
/BD {xi ⁄= yi}, where x = ( x1, . . . , xn), y = ( y1, . . . , yn) ∈ X. For
X ∈ X with independent entries, f (X) is a sub-Gaussian random variable with parameter
σ2 =∑ n
i=1 c2
i /4 for every f : X → R which is 1-Lipschitz with respect to dc by McDiarmid’s
inequality. Motivated by this example, a question of intere st is for which measures ν on
a metric space ( X, d) such that X ∼ ν, the random variable f (X) is σ2-sub-Gaussian for
every real-valued 1-Lipschitz function f : X → R. The answer to this question is given by
the aforementioned theorem of Bobkov and G¨ otze Bobkov and G¨ otze (1999). In this paper,
we focus on Lipschitz mappings f : X → Y between metric spaces ( X, dX) and ( Y, dY),
where Y ⊆ Rk and dY is any ℓp-metric for p ≥ 1. In the spirit of Marton (1986, 1996);
Bobkov and G¨ otze (1999), we prove a concentration inequali ty when a transportation cost
inequality can be shown to hold. We then provide a simple stat ionary measure estimation
example for Markov chains demonstrating that the derived in equality gives better results
than directly applying the theorem of Bobkov and G¨ otze or by combining the aforemen-
tioned theorem with Boole’s inequality. An interesting obs ervation regarding the role of the
particular ℓp-norm is also highlighted via this example.
