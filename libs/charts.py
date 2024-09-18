import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_candles(data):
    
    """
    Plots a candlestick chart with volume bars below.

    Parameters
    ----------
    data : pd.DataFrame
        A DataFrame with the following columns:
            - Date : datetime
                The date of the candle.
            - Open : float
                The opening price of the candle.
            - High : float
                The highest price of the candle.
            - Low : float
                The lowest price of the candle.
            - Close : float
                The closing price of the candle.
            - Volume : float
                The volume of the candle.

    Returns
    -------
    fig : plotly.graph_objects.Figure
        A candlestick chart with volume bars below.
    """

    data = data.iloc[-168:] # most recent 7 days
    colors = ['green' if row['Close'] > row['Open'] else 'red' for index, row in data.iterrows()]
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.7, 0.3], vertical_spacing=0.01)

    fig.update_layout(showlegend=False) # remove summary bar from ployly chart

    # Add the candlestick chart
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    ),
                row=1, col=1)

    # Add the volume bars
    fig.add_trace(
        go.Bar(
            x=data.index,
            y=data['Volume'],
            name='Volume',
            marker=dict(color=colors, opacity=0.6)
        ),
        row=2, col=1
    )

    fig.update_layout(
        height=800,  # increase height to 600 pixels
        width=1200,  # increase width to 800 pixels
        xaxis_rangeslider_visible=False,
        # title_text="ETHUSDT",
        paper_bgcolor='#000000',
        plot_bgcolor='#000000',
        font_color='white',
        xaxis=dict(gridcolor='lightgrey', gridwidth=1),
        yaxis=dict(gridcolor='lightgrey',gridwidth=1)
    )

    return fig