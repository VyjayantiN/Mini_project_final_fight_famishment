# import_excel.py

import pandas as pd
from django.core.management.base import BaseCommand
from accounts.models import recipe

class Command(BaseCommand):
    help = 'Import records from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help=r'C:\Users\nlnsa\Desktop\Mini-Project\Google_Solutions_challenge_2023-master\accounts\Finalchatgpt_dataset.xlsx')

    def handle(self, *args, **options):
        file_path = options['file_path']
        
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Iterate over rows and create recipe objects
        for index, row in df.iterrows():
            rec = recipe.objects.create(
                recipe_name=row['Recipe Name'],
                people_served=row['People Served'],
                calories=row['Calories'],
                difficulty=row['Difficulty'],
                ing=row['Ingredients'],
                ins=row['Instructions'],
                age=row['Age'],
                category=row['Category'],
                district=row['State']
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully imported recipe: {rec.recipe_name}"))
