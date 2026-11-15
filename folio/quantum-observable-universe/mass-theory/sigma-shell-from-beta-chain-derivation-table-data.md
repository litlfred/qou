| input | symbol | value at $q_0$ |
|------|------|------|
| Wedderburn coefficient | $C_{(3,2,1)}$ | ${{ qou.computations.sigma-shell-from-beta-chain.data.rows.0.C_lambda_shell | precision: 10 }}$ |
| Wenzl-bridge weight (convention D) | $y_{(3,2,1)}$ | ${{ qou.computations.sigma-shell-from-beta-chain.data.rows.0.y_lambda_shell }}$ |
| Hoefsmit character on $\beta_D$ | $\chi^{(3,2,1)}(\beta_D)$ | ${{ qou.computations.sigma-shell-from-beta-chain.data.rows.0.chi_lambda_on_beta_D | precision: 10 }}$ |
| Markov trace of deuteron braid | $\lvert\mathrm{tr}_M(\beta_D)\rvert$ | ${{ qou.computations.sigma-shell-from-beta-chain.data.rows.0.abs_tr_M_beta_D | precision: 10 }}$ |
| **Predicted** $y_{\mathrm{target}}$ | $C\cdot y \cdot \lvert\chi\rvert / \lvert\mathrm{tr}_M\rvert$ | $\mathbf{ {{ qou.computations.sigma-shell-from-beta-chain.data.rows.0.y_target_computed }} }$ |
| **Benchmark** (order-of-magnitude) | $B(D) / (2\cdot m_p)$ | ${{ qou.computations.sigma-shell-from-beta-chain.data.rows.0.y_target_benchmark_BoverAmp | precision: 4 }}$ |
| Agreement | ratio | ${{ qou.computations.sigma-shell-from-beta-chain.data.rows.0.ratio_computed_over_benchmark }}$ (benchmark not reproduced) |
