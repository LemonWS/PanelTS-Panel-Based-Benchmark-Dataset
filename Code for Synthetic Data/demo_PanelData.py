from PanelData import generate_panel_data_independent
import matplotlib.pyplot as plt
import seaborn as sns



#     N : int, Number of individuals
#     T : int, Length of time

#


panel_data = generate_panel_data_independent(N=5,                               # N : int, Number of individuals
                                             T=10000,                             # T : int, Length of time
                                             nx=5,
                                             random_trend_period=False,         # random_trend_period : bool, Enable unfixed segment length
                                             trend_period=50,                   # trend period : int, Period length
                                             trend_type='piecewise',               # trend_type : str，
                                                                                #      -linear : a single linear trend
                                                                                #      -piecewise : segmented random trend, with each segment length being a period
                                             trend_slope = None,                # trend_slope : float or None, linear trend slope, if None, randomly generated
                                             seasonal_period=12,                # seasonal_period : int, seasonal period length
                                             K=5,                               # K : int, Harmonic quantity, K determines how many frequencies are added together to form a seasonal waveform
                                             periodic=False,                    # periodic : bool, Whether to use periodic scale
                                             seed=None)                         # seed : int or None

N=5
nx = 5


filename = f"panel_#y{N}_#x{nx}.csv"
panel_data.to_csv(filename, index=False, float_format="%.4f")
print(panel_data.head(1000))


# fig, axs = plt.subplots(nx+1, 1, figsize=(10, 6), sharex=True)
#
# for entity_id in panel_data['id'].unique():
#     df_entity = panel_data[panel_data['id'] == entity_id]
#     for j in range(nx):
#         axs[j].plot(df_entity['time'], df_entity[f'x{j+1}'], label=f'Unit {entity_id+1}')
#     axs[nx].plot(df_entity['time'], df_entity['y'], label=f'Unit {entity_id+1}')
#
# for j in range(nx):
#     axs[j].set_ylabel(f'x{j+1}')
# axs[nx].set_ylabel('y')
# axs[nx].set_xlabel('Time')
#
# for ax in axs:
#     ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5),fontsize=8)
#
# plt.tight_layout(rect=[0, 0, 0.82, 1])
# plt.show()
#



#
# sns.lineplot(data=panel_data, x='time', y='y', hue='id', marker='o')
# plt.title('Panel Data y Trend by Entity')
# plt.show()


# cols_to_plot = [c for c in panel_data.columns if c not in ['id', 'time']]
#

# long_df = panel_data.melt(id_vars=['id', 'time'], value_vars=cols_to_plot,
#                          var_name='variable', value_name='value')
#

# sns.lineplot(data=long_df, x='time', y='value', hue='id', style='variable', markers=False)
# plt.title('Panel Data Trend by Entity and Variable')
# plt.show()




# x_cols = [c for c in panel_data.columns if c.startswith('x')]
# all_vars = x_cols + ['y']  # x1~xn + y
#
# n_vars = len(all_vars)
#
# # 创建子图
# fig, axs = plt.subplots(n_vars, 1, figsize=(10, 3*n_vars), sharex=True)
#
# for i, var in enumerate(all_vars):
#     ax = axs[i]
#     var_long = panel_data.melt(id_vars=['id','time'], value_vars=[var],
#                              var_name='variable', value_name='value')
#     sns.lineplot(data=var_long, x='time', y='value', hue='id', ax=ax, markers=False, legend=(i==0))
#     ax.set_title(f'Trend of {var}')
#     ax.set_ylabel(var)
#     if i < n_vars-1:
#         ax.set_xlabel('')
#     else:
#         ax.set_xlabel('Time')
#
# plt.tight_layout()
# plt.show()