# UNHCR Chart Generation MCP Server

This MCP (Model Context Protocol) server in smithery.ai provides tools for generating UNHCR charts using the FastAPI chart generation service. It allows AI agents to create various types of charts (bar, line, pie, etc.) with UNHCR data visualization.

This server interacts with the [UNHCR Chart Generation API](https://unhcrpyplot.rvibek.com.np/plot).

[![smithery badge](https://smithery.ai/badge/@rvibek/mcp-unhcrpyplot)](https://smithery.ai/server/@rvibek/mcp-unhcrpyplot)
[![smithery badge](https://smithery.ai/badge/@rvibek/mcp_unhcrpyplot)](https://smithery.ai/server/@rvibek/mcp_unhcrpyplot)

## Features

- Generate various types of charts (bar, line, pie, scatter) with UNHCR data
- Create population trend charts for refugee data
- Generate comparison charts with multiple datasets
- Customize chart titles, labels, and styling
- Return charts as base64-encoded images for easy integration

## Connect to MCP Server

To access the server, open your web browser and visit the following URL:
[https://smithery.ai/server/@rvibek/mcp_unhcrpyplot](https://smithery.ai/server/@rvibek/mcp_unhcrpyplot)

Configure the MCP host/client as needed.

## API Endpoint

The server generates charts using the following API endpoint:
- `https://unhcrpyplot.rvibek.com.np/plot`

The API accepts JSON payloads with the following structure:
```json
{
  "chart_type": "string",
  "title": "string",
  "subtitle": "string",
  "x_label": "string",
  "y_label": "string",
  "data": {
    "labels": ["string"],
    "values": [number]
  }
}
```

## MCP Tools

The server exposes the following tools:

### `generate_unhcr_graph`

Generate a UNHCR chart using the FastAPI chart generation service.

**Parameters:**
- `chart_type` (required): Type of chart to generate (bar, line, pie, scatter, etc.)
- `title` (required): Main title of the chart
- `subtitle` (required): Subtitle describing the chart content
- `x_label` (required): Label for the x-axis
- `y_label` (required): Label for the y-axis
- `labels` (required): List of labels for the data points (e.g., years, countries)
- `values` (required): List of numerical values corresponding to the labels

**Returns:**
- Dictionary containing the chart image as base64 and metadata

### `generate_comparison_chart`

Generate a comparison chart with multiple datasets.

**Parameters:**
- `chart_type` (required): Type of chart (bar, line, etc.)
- `title` (required): Main title of the chart
- `subtitle` (required): Subtitle describing the chart content
- `x_label` (required): Label for the x-axis
- `y_label` (required): Label for the y-axis
- `datasets` (required): List of datasets, each containing 'label', 'labels', and 'values'

**Returns:**
- Dictionary containing the chart image as base64 and metadata

### `generate_population_trend_chart`

Generate a population trend chart for UNHCR data.

**Parameters:**
- `years` (required): List of years for the x-axis
- `population_counts` (required): List of population counts for each year
- `country_name` (optional): Name of the country or region being visualized (default: "Country")
- `chart_type` (optional): Type of chart (line, bar, etc.) (default: "line")

**Returns:**
- Dictionary containing the chart image as base64 and metadata

## Example Usage

Here's an example of how to use the `generate_unhcr_graph` tool:

```python
# Generate a bar chart showing refugee population trends
result = generate_unhcr_graph(
    chart_type="bar",
    title="Nepali Refugees and Asylum Seekers in Canada (2020-2021)",
    subtitle="UNHCR Population Data",
    x_label="Year",
    y_label="Number of People",
    labels=["2020", "2021"],
    values=[205, 114]
)
```

## Response Format

Successful chart generation returns:
```json
{
  "status": "success",
  "chart_type": "bar",
  "title": "Chart Title",
  "image_base64": "base64_encoded_image_string",
  "image_format": "png",
  "message": "Successfully generated bar chart: Chart Title"
}
```

## License

MIT

## Acknowledgments

This project uses the [UNHCR Chart Generation API](https://unhcrpyplot.rvibek.com.np/plot) for creating visualizations of UNHCR data.