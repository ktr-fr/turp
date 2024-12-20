import gradio as gr
import subprocess
import folium

def calculate_distances(x1, y1, x2, y2):
    process = subprocess.Popen(['./distance_calc'], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               text=True)
    output, _ = process.communicate(f"{x1}\n{y1}\n{x2}\n{y2}\n")
    euclidean, manhattan, chebyshev = map(float, output.strip().split('\n'))
    
    m = folium.Map(location=[(y1+y2)/2, (x1+x2)/2], zoom_start=10)
    folium.Marker([y1, x1], popup="Point 1").add_to(m)
    folium.Marker([y2, x2], popup="Point 2").add_to(m)
    folium.PolyLine(locations=[[y1, x1], [y2, x2]], color="red", weight=2, opacity=0.8).add_to(m)
    
    m.save("map.html")
    
    return f"Euclidean: {euclidean:.2f}", f"Manhattan: {manhattan:.2f}", f"Chebyshev: {chebyshev:.2f}", "map.html"

iface = gr.Interface(
    fn=calculate_distances,
    inputs=[
        gr.Number(label="X1"),
        gr.Number(label="Y1"),
        gr.Number(label="X2"),
        gr.Number(label="Y2")
    ],
    outputs=[
        gr.Text(label="Euclidean Distance"),
        gr.Text(label="Manhattan Distance"),
        gr.Text(label="Chebyshev Distance"),
        gr.HTML(label="Map")
    ],
    title="Distance Calculator",
    description="Calculate Euclidean, Manhattan, and Chebyshev distances between two points"
)

iface.launch()
