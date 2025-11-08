# Deployment Guide for UNHCR Chart Generation MCP Server

This guide explains how to deploy the MCP server to Smithery.

## Prerequisites

- GitHub account
- Smithery account
- Python 3.12+ environment with MCP libraries

## Deployment Steps

### 1. Push to GitHub

First, push your code to a GitHub repository:

```bash
git init
git add .
git commit -m "Initial commit: UNHCR Chart Generation MCP Server"
git branch -M main
git remote add origin https://github.com/yourusername/mcp_unhcrpyplot.git
git push -u origin main
```

### 2. Deploy to Smithery

1. Visit [Smithery](https://smithery.ai)
2. Click "Add Server" 
3. Select "GitHub" as the source
4. Choose your repository: `yourusername/mcp_unhcrpyplot`
5. Configure the server:
   - **Runtime**: Python
   - **Server Entry Point**: `mcp_unhcrpyplot.server:create_server`
   - **Package Name**: `mcp_unhcrpyplot`

### 3. Verify Deployment

After deployment, you can access your MCP server at:
```
https://smithery.ai/server/@yourusername/mcp_unhcrpyplot
```

## Testing the Server

You can test the server using the Smithery playground or by integrating it with an MCP client.

### Example Usage

```python
# Using the generate_unhcr_graph tool
result = generate_unhcr_graph(
    chart_type="bar",
    title="Refugee Population Trends",
    subtitle="UNHCR Data 2020-2024",
    x_label="Year",
    y_label="Population",
    labels=["2020", "2021", "2022", "2023", "2024"],
    values=[1000, 1200, 1500, 1800, 2000]
)

# The result will contain a base64-encoded PNG image
if result["status"] == "success":
    image_data = result["image_base64"]
    # Use the image data as needed
```

## Available Tools

1. **generate_unhcr_graph** - Generate basic charts with labels and values
2. **generate_comparison_chart** - Generate charts with multiple datasets
3. **generate_population_trend_chart** - Generate population trend charts

## Troubleshooting

- If deployment fails, check that all dependencies are properly specified in `pyproject.toml`
- Ensure the server entry point is correctly configured in `pyproject.toml`
- Verify that the FastAPI endpoint `https://unhcrpyplot.rvibek.com.np/plot` is accessible

## Support

For issues with deployment, refer to the [Smithery documentation](https://smithery.ai/docs).
