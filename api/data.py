import pandas as pd
import os
import json

# This file contains sample data or handles data loading for Vercel environment

def get_sample_data():
    """
    Generate sample data if real data files aren't available
    (useful for Vercel deployment)
    """
    # Sample France data
    france_data = {
        'url': ['https://chatgpt.com/'] * 5,
        'prompt': [
            'What role does acoustic performance play in modern office redesign?',
            'What design strategies help reduce disruptive noise in the office environment?',
            'How can a well-designed office space balance collaboration and individual focus?',
            'What are acoustic pods and how do they work?',
            'Are acoustic pods from workwithisland.com energy efficient?'
        ],
        'country': ['France'] * 5,
        'response': [
            'Acoustic performance plays a crucial role in modern office redesign by directly impacting employee productivity, wellbeing, and satisfaction. As open-plan offices have become prevalent, controlling noise has become a significant challenge...',
            'Several design strategies can effectively reduce disruptive noise in office environments. These include: 1) Acoustic barriers and panels, 2) Sound-absorbing materials, 3) Strategic space planning, 4) Incorporation of acoustic pods and booths...',
            'Balancing collaboration and individual focus in office design requires thoughtful space planning that acknowledges different work modes. Effective strategies include: 1) Creating designated zones for different activities, 2) Incorporating acoustic solutions like pods...',
            'Acoustic pods are self-contained, insulated spaces designed to create quiet environments within open offices. They work by using sound-absorbing materials, sealed construction, and sometimes active noise cancellation to create private spaces for calls or focused work...',
            'Acoustic pods from workwithisland.com are designed with sustainability and energy efficiency as core features. They incorporate LED lighting, motion sensors for automatic power management, and use recycled materials in their construction...'
        ],
        'brand_mentioned': [False, False, False, False, True],
        'visibule': [False, False, False, False, True],
        'branded': [False, False, False, False, True]
    }

    # Sample Countries data
    countries_data = {
        'url': ['https://chatgpt.com/'] * 10,
        'prompt': [
            'In France what role does acoustic performance play in modern office redesign?',
            'In the UK what are acoustic pods and how do they work?',
            'In Spain how can a well-designed office space balance collaboration and individual focus?',
            'In Switzerland what design strategies help reduce disruptive noise?',
            'In Benelux are acoustic pods energy efficient?',
            'In France are acoustic pods from workwithisland.com energy efficient?',
            'In the UK what are the advantages of workwithisland.com acoustic booths?',
            'In Spain how do workwithisland.com products integrate with office design?',
            'In Switzerland what materials are used in workwithisland.com acoustic pods?',
            'In Benelux are workwithisland.com acoustic pods comfortable for extended use?'
        ],
        'country': ['France', 'United Kingdom', 'Spain', 'Switzerland', 'Benelux', 
                   'France', 'United Kingdom', 'Spain', 'Switzerland', 'Benelux'],
        'response': [
            'In France, acoustic performance is considered essential in modern office redesign, reflecting the country\'s strong emphasis on worker wellbeing and productivity...',
            'In the UK, acoustic pods are increasingly popular solutions for open plan offices. These self-contained units provide private spaces for calls, meetings, or focused work...',
            'Spanish office design emphasizes a balance between collaborative and focused work through thoughtful space planning that respects different work styles and needs...',
            'Swiss design strategies for noise reduction typically incorporate precision-engineered solutions including strategic space planning, acoustic barriers, and sound-absorbing materials...',
            'In Benelux countries, energy efficiency is a primary consideration in office design, and acoustic pods generally incorporate energy-saving features like LED lighting and motion sensors...',
            'Acoustic pods from workwithisland.com available in France are designed with sustainability and energy efficiency as key features, aligning with French environmental standards...',
            'In the UK, workwithisland.com acoustic booths offer significant advantages including exceptional sound isolation, flexible placement, modern aesthetic design, and integration with digital tools...',
            'In Spain, workwithisland.com products are designed to integrate seamlessly with modern office landscapes, offering flexible solutions that complement open-plan designs...',
            'Workwithisland.com acoustic pods available in Switzerland use premium materials including acoustic foam, sound-dampening fabrics, and environmentally sustainable wood products...',
            'In Benelux countries, workwithisland.com acoustic pods are designed for comfort during extended use, featuring ergonomic seating, appropriate ventilation, and adjustable lighting...'
        ],
        'brand_mentioned': [False, False, False, False, False, True, True, True, True, True],
        'visibule': [False, False, False, False, False, True, True, True, True, True],
        'branded': [False, False, False, False, False, True, True, True, True, True]
    }

    # Sample Personas data
    personas_data = {
        'url': ['https://chatgpt.com/'] * 10,
        'prompt': [
            'As a CEO how can acoustic solutions improve my company\'s productivity?',
            'As an HR Manager what impact do acoustic pods have on employee wellbeing?',
            'As an Interior Architect how do I integrate acoustic booths with office design?',
            'As an Office Manager how quickly can acoustic pods be installed?',
            'As a Startup Founder what\'s the ROI for investing in acoustic solutions?',
            'As a CEO are workwithisland.com acoustic pods worth the investment?',
            'As an HR Manager how do workwithisland.com products affect employee satisfaction?',
            'As an Interior Architect what design options does workwithisland.com offer?',
            'As an Office Manager how easy are workwithisland.com pods to maintain?',
            'As a Startup Founder can workwithisland.com acoustic booths scale with my company?'
        ],
        'country': ['France', 'United Kingdom', 'Spain', 'Switzerland', 'Benelux',
                   'France', 'United Kingdom', 'Spain', 'Switzerland', 'Benelux'],
        'persona': ['CEO', 'HR Manager', 'Interior Architect', 'Office Manager', 'Startup Founder',
                   'CEO', 'HR Manager', 'Interior Architect', 'Office Manager', 'Startup Founder'],
        'response': [
            'As a CEO, investing in acoustic solutions can significantly improve company productivity by reducing noise distractions that impact concentration and cognitive performance...',
            'As an HR Manager, you\'ll find that acoustic pods have a substantial positive impact on employee wellbeing by reducing noise stress, providing privacy for sensitive conversations, and offering spaces for mental breaks...',
            'As an Interior Architect, integrating acoustic booths with office design requires thoughtful placement to complement traffic flow, visual harmony with the overall design language, and consideration of technical requirements...',
            'As an Office Manager, you\'ll be pleased to know that modern acoustic pods can typically be installed within 1-2 days with minimal disruption to the office environment...',
            'As a Startup Founder, the ROI for acoustic solutions comes from increased productivity, improved talent retention, enhanced company image, and more efficient use of office space...',
            'As a CEO, workwithisland.com acoustic pods represent a strategic investment that can deliver returns through improved employee productivity, enhanced company image, and flexible space utilization...',
            'As an HR Manager, workwithisland.com products have been shown to positively impact employee satisfaction by providing quiet spaces for focus, reducing noise stress, and demonstrating company investment in wellbeing...',
            'As an Interior Architect, workwithisland.com offers a range of design options with customizable exteriors, various size configurations, and integration possibilities with existing design elements...',
            'As an Office Manager, you\'ll find workwithisland.com pods are designed for easy maintenance with wipeable surfaces, replaceable components, and minimal technical upkeep requirements...',
            'As a Startup Founder, workwithisland.com acoustic booths are designed with scalability in mind, offering modular options that can be added to as your company grows...'
        ],
        'brand_mentioned': [False, False, False, False, False, True, True, True, True, True],
        'visibule': [False, False, False, False, False, True, True, True, True, True],
        'branded': [False, False, False, False, False, True, True, True, True, True]
    }

    # Convert to DataFrames
    df_france = pd.DataFrame(france_data)
    df_countries = pd.DataFrame(countries_data)
    df_personas = pd.DataFrame(personas_data)
    
    return df_france, df_countries, df_personas

def get_data():
    """
    Try to load actual data files, fall back to sample data if they don't exist
    """
    try:
        # Try to load the real data files
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        df_france = pd.read_csv(os.path.join(base_dir, 'workwithisland_questions_france_enriched.csv'))
        df_countries = pd.read_csv(os.path.join(base_dir, 'workwithisland_questions_countries_enriched.csv'))
        df_personas = pd.read_csv(os.path.join(base_dir, 'workwithisland_questions_personas_enriched.csv'))
        
        return df_france, df_countries, df_personas
    except:
        # If any error occurs, use sample data
        print("Using sample data for Vercel deployment")
        return get_sample_data() 