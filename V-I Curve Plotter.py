import plotly.graph_objects as go
import numpy as np

vm_volts = np.array([
    -2, -3, -3.92, -4.19, -4.40, -4.52, -4.66, -4.75, -4.82, -4.88,
    -4.94, -4.97, -5.05, -5.09, -5.14, -5.18, -5.2, -5.22, -5.24, -5.27
])
ia_milliamps = np.array([
    0, 0, -0.04, -0.09, -0.14, -0.21, -0.30, -0.43, -0.58, -0.67,
    -0.84, -1.00, -1.45, -1.91, -2.86, -4.82, -7.90, -10.97, -15.02, -19.83
])

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=vm_volts,
    y=ia_milliamps,
    mode='lines+markers',
    name='Measured Data',
    line=dict(color='#1f77b4')
))

fig.update_layout(
    title='V–I Characteristic Curve',
    xaxis_title='Voltage across device, Vm (V)',
    yaxis_title='Current through device, IA (mA)',
    xaxis=dict(
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='black',
        range=[-6, 6],
    ),
    yaxis=dict(
        zeroline=True,
        zerolinewidth=2,
        zerolinecolor='black',
        range=[-22, 22],
    ),
    plot_bgcolor='white',
    hovermode='x unified',
    width=900,
    height=600
)

fig.show()
