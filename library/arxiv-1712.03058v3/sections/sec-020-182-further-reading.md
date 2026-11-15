---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-020-182-further-reading
section_title: "Further reading"
section_number: 1.8.2
pages: 25-29
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
Further reading
For the reader interested in more details about the theoretical background
of iterated ﬁltering methods we recommend Ionides et al. (2006) and Ionides
et al. (2015) for further reading. For the reader interested in learning how
to work with the R package pomp we recommend the study of King et al.
(2016) and to follow some of the very comprehensive online tutorials available
through King (2017). The package has already been applied to answer many
diﬀerent epidemiological questions for diﬀerent infectious diseases, e.g. for
cholera (King et al., 2008), measles (He et al., 2010), malaria (Bhadra et al.,
2011), polio (Martinez-Bakker et al., 2015), ebola (King et al., 2015a), and
rotavirus (Martinez et al., 2016; Stocks et al., 2018). Finally, iterated ﬁltering
has facilitated the development and analysis of a divers array of mechanistic
models, a recent and comprehensive review of which can be found in Bretó
(2017).
Acknowledgments
I would like to thank Aaron A. King for making the tutorials and, espe-
cially, the codes in King (2017) available. Furthermore, I would like to thank
Carles Bretó and Philip O’Neill for their constructive comments and sug-
gestions. TS was supported by the Swedish research council, grant number
2015_05182_VR.
Bibliography
Andrieu, C., Doucet, A., and Holenstein, R. (2010). Particle Markov chain
Monte Carlo methods. Journal of the Royal Statistical Society: Series B,
72(3):269–342.
Arulampalam, M. S., Maskell, S., Gordon, N., and Clapp, T. (2002). A tuto-
rial on particle ﬁlters for online nonlinear, non-Gaussian Bayesian tracking.
IEEE Transactions on Signal Processing, 50(2):174–188.
Atkins, K. E., Shim, E., Pitzer, V. E., and Galvani, A. P. (2012). Impact of
rotavirus vaccination on epidemiological dynamics in England and Wales.
Vaccine, 30(3):552–564.
Bhadra, A., Ionides, E. L., Laneri, K., Pascual, M., Bouma, M., and Dhi-
man, R. (2011). Malaria in northwest India: Data analysis via partially ob-
served stochastic diﬀerential equation models driven by Lévy noise. Journal
of the American Statistical Association, 106(494):440–451.
Bretó, C. (2017). Modeling and inference for infectious disease dynamics:
a likelihood-based approach. Statistical Science, (In press, http://www.
imstat.org/sts/STS636.pdf).
Bretó, C., He, D., Ionides, E. L., and King, A. A. (2009). Time series analysis
via mechanistic models. The Annals of Applied Statistics, 3(1):319–348.
Bretó, C. and Ionides, E. L. (2011). Compound Markov counting processes
and their applications to modeling inﬁnitesimally over-dispersed systems.
Stochastic Processes and Their Applications, 121(11):2571–2591.
Del Moral, P. (1996).
Non linear ﬁltering: Interacting particle solution.
Markov Processes and Related Fields, 2(4):555–580.
Doucet, A., de Freitas, N., and Gordon, N. (2001). Sequential Monte Carlo
Methods in Practice. Springer-Verlag, New York.
25
BIBLIOGRAPHY
26
Doucet, A. and Johansen, A. M. (2011). A tutorial on particle ﬁltering and
smoothing: ﬁfteen years later. Oxford Handbook of nonlinear ﬁltering.
Erhard, F., Friedel, C. C., and Zimmer, R. (2010). FERN- Stochastic Simu-
lation and Evaluation of Reaction Networks. Systems Biology for Signaling
Networks.
Fuchs, C. (2013). Inference for Diﬀusion Processes- With Applications in
Life Sciences. Springer-Verlag Berlin Heidelberg.
Gibbons, C. L., Mangen, M. J., Plass, D., Havelaar, A. H., Brooke, R. J.,
Kramarz, P., Peterson, K. L., Stuurman, A. L., Cassini, A., Fèvre, E. M.,
and Kretzschmar, M. E. (2014).
Measuring underreporting and under-
ascertainment in infectious disease datasets: a comparison of methods.
BMC Public Health, 14(147).
Gillespie, D. T. (1977).
Exact stochastic simulation of coupled chemical
reactions. The Journal of Physical Chemistry, 81(25):2340–2361.
Gillespie, D. T. (2001). Approximate accelerated stochastic simulation of
chemically reacting systems. Journal of Chemical Physics, 115(4):1716–
1733.
He, D., Ionides, E. L., and King, A. A. (2010). Plug-and-play inference for
disease dynamics: Measles in large and small populations as a case study.
Journal of the Royal Society Interface, 7(43):271–283.
Held, L. and Sabanés Bové, D. (2013). Applied Statistical Inference. Springer.
Ionides, E. L., Bretó, C., and King, A. A. (2006). Inference for nonlinear
dynamical systems. PNAS, 103(49):18438–18443.
Ionides, E. L., Bretó, C., Park, J., Smith, R. A., and King, A. A. (2017).
Monte Carlo proﬁle conﬁdence intervals for dynamic systems. Journal of
The Royal Society Interface, 14(132).
Ionides, E. L., Nguyen, D., Atchadé, Y., Stoev, S., and King, A. (2015).
Inference for dynamic and latent variable models via iterated, perturbed
Bayes maps. PNAS, 112(3):719–724.
Karlin, S. and Taylor, H. M. (1981). A Second Course in Stochastic Processes.
Academic Press.
Keeling, M. J. and Rohani, P. (2008). Modeling Infectious Diseases in Hu-
mans and Animals. Princeton University Press.
BIBLIOGRAPHY
27
Kendall, B. E., Briggs, C. J., Murdoch, W. W., Turchin, P., Ellner , S. P.,
McCauley, E., Nisbet, R. M., and Wood, S. N. (1999). Why do populations
cycle?
A synthesis of statistical and mechanistic modeling approaches.
Ecology, 80(6):1789–1805.
King, A. A. (2017). Project pomp on github. http://kingaa.github.io/pomp/,
[Accessed September 15, 2017].
King, A. A., Domenech de Cellès, M., Magpantay, F. M. G., and Rohani,
P. (2015a). Avoidable errors in the modelling of outbreaks of emerging
pathogens, with special reference to Ebola. Proceedings of the Royal Society
of London B, 282:20150347.
King, A. A., Ionides, E. L., Bretó, C., Ellner, S., Kendall, B., Ferrari, M.,
Lavone, M., and Reuman, D. (2015b). Introduction to pomp: Inference
for partially-observed Markov processes. R vignette.
King, A. A., Ionides, E. L., Pascual, M., and Bouma, M. J. (2008). Inapparent
infections and cholera dynamics. Nature, 454:877–888.
King, A. A., Nguyen, D., and Ionides, E. L. (2016). Statistical inference for
partially observed Markov processes via the R package pomp. Journal of
Statistical Software, 69(12):1–43.
Kitagawa,
G. (1987).
Non-gaussian state-space modeling of nonsta-
tionary time series.
Journal of the American Statistical Association,
82(400):1032–1041.
Liu, J. and West, M. (2001). Combinig parameter and state estimation in
simulation-based ﬁltering. Sequential Monte Carlo Methods in Practice,
pages 197–223.
Martinez, P. P., King, A. A., Yunusd, M., Faruqued, A. S. G., and Pascual,
M. (2016). Diﬀerential and enhanced response to climate forcing in diar-
rheal disease due to rotavirus across a megacity of the developing world.
PNAS, 113(15):4092–4097.
Martinez-Bakker, M., King, A. A., and Rohani, P. (2015). Unraveling the
transmission ecology of polio. PLOS Biology, 13(6):e1002172.
McCullagh, R. and Nelder, J. (1989). Generalized Linear Models. 2nd ed.
Chapman and Hall, London.
Nelder, J. A. and Mead, R. (1965). A simplex method for function minimiza-
tion. The Computer Journal, 7(4):308–313.
BIBLIOGRAPHY
28
Nocedal, J. and Wright, S. J., editors (1999).
Numerical Optimization.
Springer Series in Operations Research and Financial Engineering.
Pawitan, Y. (2001). In All Likelihood: Statistical Modelling and Inference
Using Likelihood. Oxford University Press.
Robert, C. P. and Casella, G. (2004).
Monte Carlo Statistical Methods.
Springer-Verlag.
Stocks, T. (2017).
Chapter on iterated ﬁltering methods on github.
https://github.com/theresasophia/chapter_IFmethods, [Accessed October
27, 2018].
Stocks, T., Britton, T., and Höhle, M. (2018). Model selection and parameter
estimation for dynamic epidemic models via iterated ﬁltering: application
to rotavirus in Germany. Biostatistics, page kxy057.
Stoer, J. and Bulirsch, R. (2002).
Introduction to Numerical Analysis.
Springer.
Sugihara, G. and May, R. M. (1990).
Nonlinear forecasting as a way
of distinguishing chaos from measurement error in time series. Nature,
344(6268):734–741.
Toni, T., Welch, D., Strelkowa, N., Ipsen, A., and Stumpf, M. P. (2009).
Approximate Bayesian computation scheme for parameter inference and
model selection in dynamical systems. Journal of the Royal Society Inter-
face, 6(31).
Weidemann, F., Dehnert, M., Koch, J., Wichmann, O., and Höhle, M. (2013).
Bayesian parameter inference for dynamic infectious disease modeling: ro-
tavirus in Germany. Statistics in Medicine, 33(9):1580–1599.
Wilks, S. S. (1938). The large-sample distribution of the likelihood ratio
for testing composite hypotheses. The Annals of Mathematical Statistics,
1(9):60–62.
Wood, S. N. (2010). Statistical inference for noisy nonlinear ecological dy-
namic systems. Nature, 466(7310):1102–1104.
