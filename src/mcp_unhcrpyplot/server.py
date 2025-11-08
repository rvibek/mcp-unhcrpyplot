#!/usr/bin/env python3
"""
UNHCR Chart Generation MCP Server

This MCP server provides tools for generating UNHCR charts using the FastAPI chart generation service.
It allows creating various types of charts (bar, line, pie, etc.) with UNHCR data visualization.

API Endpoint: https://unhcrpyplot.rvibek.com.np/plot
"""

import base64
import logging
from typing import Any, Dict, List, Optional

import requests
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from smithery.decorators import smithery

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ConfigSchema(BaseModel):
    pass

@smithery.server(config_schema=ConfigSchema)
def create_server():
    """Create and return a FastMCP server instance."""

    server = FastMCP(name="UNHCR Chart Generator")

    def generate_chart(chart_type: str, title: str, subtitle: str, x_label: str, y_label: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a chart using the FastAPI chart generation service.
        
        Args:
            chart_type: Type of chart (bar, line, pie, scatter, etc.)
            title: Main title of the chart
            subtitle: Subtitle of the chart
            x_label: Label for x-axis
            y_label: Label for y-axis
            data: Chart data containing labels and values
            
        Returns:
            Dictionary containing the chart image as base64 or error information
        """
        payload = {
            "chart_type": chart_type,
            "title": title,
            "subtitle": subtitle,
            "x_label": x_label,
            "y_label": y_label,
            "data": data
        }
        
        url = "https://unhcrpyplot.rvibek.com.np/plot"
        
        try:
            logger.info(f"Generating {chart_type} chart: {title}")
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            # Return the image as base64
            image_base64 = base64.b64encode(response.content).decode('utf-8')
            
            # Create Markdown format for clients that can render images
            markdown_preview = f"![{title}](data:image/png;base64,{image_base64})"
            
            return {
                "status": "success",
                "chart_type": chart_type,
                "title": title,
                # "image_base64": image_base64,
                "image_format": "png",
                "markdown_preview": markdown_preview,
                "message": f"Successfully generated {chart_type} chart: {title}"
            }
            
        except requests.RequestException as e:
            logger.error(f"Error generating chart: {e}")
            return {
                "status": "error",
                "error": str(e),
                "message": f"Failed to generate chart: {title}"
            }

    @server.tool()
    def generate_unhcr_graph(
        chart_type: str,
        title: str,
        subtitle: str,
        x_label: str,
        y_label: str,
        labels: List[str],
        values: List[float]
    ) -> Dict[str, Any]:
        """
        Generate a UNHCR chart using the FastAPI chart generation service.
        
        Args:
            chart_type: Type of chart to generate (bar, line, pie, scatter, etc.)
            title: Main title of the chart
            subtitle: Subtitle describing the chart content
            x_label: Label for the x-axis
            y_label: Label for the y-axis
            labels: List of labels for the data points (e.g., years, countries)
            values: List of numerical values corresponding to the labels
            
        Returns:
            Dictionary containing the chart image as base64 and metadata
        """
        data = {
            "labels": labels,
            "values": values
        }
        
        return generate_chart(chart_type, title, subtitle, x_label, y_label, data)

    @server.tool()
    def generate_comparison_chart(
        chart_type: str,
        title: str,
        subtitle: str,
        x_label: str,
        y_label: str,
        datasets: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Generate a comparison chart with multiple datasets.
        
        Args:
            chart_type: Type of chart (bar, line, etc.)
            title: Main title of the chart
            subtitle: Subtitle describing the chart content
            x_label: Label for the x-axis
            y_label: Label for the y-axis
            datasets: List of datasets, each containing 'label', 'labels', and 'values'
            
        Returns:
            Dictionary containing the chart image as base64 and metadata
        """
        data = {
            "datasets": datasets
        }
        
        return generate_chart(chart_type, title, subtitle, x_label, y_label, data)

    @server.tool()
    def generate_population_trend_chart(
        years: List[str],
        population_counts: List[float],
        country_name: str = "Country",
        chart_type: str = "line"
    ) -> Dict[str, Any]:
        """
        Generate a population trend chart for UNHCR data.
        
        Args:
            years: List of years for the x-axis
            population_counts: List of population counts for each year
            country_name: Name of the country or region being visualized
            chart_type: Type of chart (line, bar, etc.)
            
        Returns:
            Dictionary containing the chart image as base64 and metadata
        """
        title = f"{country_name} Refugee Population Trends"
        subtitle = "UNHCR Population Data Over Time"
        x_label = "Year"
        y_label = "Population Count"
        
        data = {
            "labels": years,
            "values": population_counts
        }
        
        return generate_chart(chart_type, title, subtitle, x_label, y_label, data)

    return server
