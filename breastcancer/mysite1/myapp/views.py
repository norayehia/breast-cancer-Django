from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
# Create your views here.
from django.shortcuts import render

#from joblib import load
#check templates in settings
#2after make html then 3 url in app then url in my site then run
"""
def predictor(request):
    
    return render(request, 'main.html')
    #return render(request, 'main.html')

"""





    
"""
#model = load('./savedModels/model.joblib')


def predictor(request):
    if request.method == 'POST':
        radius_mean = request.POST['radius_mean']
        texture_mean = request.POST['texture_mean']
        perimeter_mean = request.POST['perimeter_mean']
        area_mean = request.POST['area_mean']

        smoothness_mean = request.POST['smoothness_mean']
        compactness_mean = request.POST['compactness_mean']
        concavity_mean = request.POST['concavity_mean']
        concavepoints_mean = request.POST['concavepoints_mean']
        symmetry_mean = request.POST['symmetry_mean']
        Fractal_dimension_mean = request.POST['Fractal_dimension_mean']
        Radius_se = request.POST['Radius_se']
        Texture_se = request.POST['Texture_se']
        Perimeter_se = request.POST['Perimeter_se']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']
        area_mean = request.POST['area_mean']









        #Feature Scaling
        sc = StandardScaler()
        X_test = sc.transform([[radius_mean, texture_mean, perimeter_mean, area_mean,smoothness_mean,compactness_mean,concavepoints_mean,,,,,,,,,,,,,,,,,,,,,,,,,,,]])
        y_pred = model.predict(X_test)
        y_pred = (y_pred > 0.5)
       
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')

"""
"""
        if y_pred[0] == 0:
            y_pred = 'Setosa'
        elif y_pred[0] == 1:
            y_pred = 'Verscicolor'
        else:
            y_pred = 'Virginica'
            """


"""

from sklearn.preprocessing import StandardScaler
from .models import BreastCancerData
from keras.models import load_model

model = load_model('F:/projectsdjan/savedmodel/model_breast.h5')
def predictor(request):
    if request.method == 'POST':
        radius_mean = request.POST['radius_mean']
        texture_mean = request.POST['texture_mean']
        perimeter_mean = request.POST['perimeter_mean']
        area_mean = request.POST['area_mean']
        smoothness_mean = request.POST['smoothness_mean']
        compactness_mean = request.POST['compactness_mean']
        concavity_mean = request.POST['concavity_mean']
        concavepoints_mean = request.POST['concavepoints_mean']
        symmetry_mean = request.POST['symmetry_mean']
        fractal_dimension_mean = request.POST['fractal_dimension_mean']
        radius_se = request.POST['radius_se']
        texture_se = request.POST['texture_se']
        perimeter_se = request.POST['perimeter_se']
        area_se = request.POST['area_se']
        smoothness_se = request.POST['smoothness_se']
        compactness_se = request.POST['compactness_se']
        concavity_se = request.POST['concavity_se']
        concavepoints_se = request.POST['concavepoints_se']
        symmetry_se = request.POST['symmetry_se']
        fractal_dimension_se = request.POST['fractal_dimension_se']
        radius_worst = request.POST['radius_worst']
        texture_worst = request.POST['texture_worst']
        perimeter_worst = request.POST['perimeter_worst']
        area_worst = request.POST['area_worst']
        smoothness_worst = request.POST['smoothness_worst']
        compactness_worst = request.POST['compactness_worst']
        concavity_worst = request.POST['concavity_worst']
        concavepoints_worst = request.POST['concavepoints_worst']
        symmetry_worst = request.POST['symmetry_worst']
        fractal_dimension_worst = request.POST['fractal_dimension_worst']

        # Feature Scaling
        


        sc = StandardScaler()
        X_test = sc.transform([[radius_mean, texture_mean, perimeter_mean, area_mean,
                                smoothness_mean, compactness_mean, concavity_mean, concavepoints_mean,
                                symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se,
                                area_se, smoothness_se, compactness_se, concavity_se, concavepoints_se,
                                symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
                                perimeter_worst, area_worst, smoothness_worst, compactness_worst,
                                concavity_worst, concavepoints_worst, symmetry_worst, fractal_dimension_worst]])
        
        y_pred = model.predict(X_test)
        y_pred = (y_pred > 0.5)
       
        return render(request, 'main.html', {'result': y_pred})
    
    return render(request, 'main.html')



"""
from sklearn.preprocessing import StandardScaler
from .models import BreastCancerData
from keras.models import load_model

model = load_model('F:/projectsdjan/savedmodel/model_breast.h5')

def predictor(request):
    if request.method == 'POST':
        features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
                    'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concavepoints_mean',
                    'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se',
                    'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concavepoints_se',
                    'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
                    'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst',
                    'concavity_worst', 'concavepoints_worst', 'symmetry_worst', 'fractal_dimension_worst']

        input_data = []
        for feature in features:
            value = request.POST.get(feature, 0)  # Get the value or use 0 as default
            input_data.append(float(value))

        # Feature Scaling
        #sc = StandardScaler()
        #X_test = sc.transform([input_data])

        y_pred = model.predict([input_data])
        y_pred = (y_pred > 0.5)

        return render(request, 'main.html', {'result': y_pred})

    return render(request, 'main.html')