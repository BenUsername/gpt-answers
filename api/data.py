import os
import json

# This file contains sample data for Vercel deployment

def get_sample_data():
    """
    Generate sample data using plain Python data structures
    """
    # Sample France data as a list of dictionaries
    france_data = [
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'What role does acoustic performance play in modern office redesign?',
            'country': 'France',
            'response': 'Acoustic performance plays a crucial role in modern office redesign by directly impacting employee productivity, wellbeing, and satisfaction. As open-plan offices have become prevalent, controlling noise has become a significant challenge...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'What design strategies help reduce disruptive noise in the office environment?',
            'country': 'France',
            'response': 'Several design strategies can effectively reduce disruptive noise in office environments. These include: 1) Acoustic barriers and panels, 2) Sound-absorbing materials, 3) Strategic space planning, 4) Incorporation of acoustic pods and booths...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'How can a well-designed office space balance collaboration and individual focus?',
            'country': 'France',
            'response': 'Balancing collaboration and individual focus in office design requires thoughtful space planning that acknowledges different work modes. Effective strategies include: 1) Creating designated zones for different activities, 2) Incorporating acoustic solutions like pods...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'What are acoustic pods and how do they work?',
            'country': 'France',
            'response': 'Acoustic pods are self-contained, insulated spaces designed to create quiet environments within open offices. They work by using sound-absorbing materials, sealed construction, and sometimes active noise cancellation to create private spaces for calls or focused work...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'Are acoustic pods from workwithisland.com energy efficient?',
            'country': 'France',
            'response': 'Acoustic pods from workwithisland.com are designed with sustainability and energy efficiency as core features. They incorporate LED lighting, motion sensors for automatic power management, and use recycled materials in their construction...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        }
    ]

    # Sample Countries data
    countries_data = [
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In France what role does acoustic performance play in modern office redesign?',
            'country': 'France',
            'response': 'In France, acoustic performance is considered essential in modern office redesign, reflecting the country\'s strong emphasis on worker wellbeing and productivity...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In the UK what are acoustic pods and how do they work?',
            'country': 'United Kingdom',
            'response': 'In the UK, acoustic pods are increasingly popular solutions for open plan offices. These self-contained units provide private spaces for calls, meetings, or focused work...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In Spain how can a well-designed office space balance collaboration and individual focus?',
            'country': 'Spain',
            'response': 'Spanish office design emphasizes a balance between collaborative and focused work through thoughtful space planning that respects different work styles and needs...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In Switzerland what design strategies help reduce disruptive noise?',
            'country': 'Switzerland',
            'response': 'Swiss design strategies for noise reduction typically incorporate precision-engineered solutions including strategic space planning, acoustic barriers, and sound-absorbing materials...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In Benelux are acoustic pods energy efficient?',
            'country': 'Benelux',
            'response': 'In Benelux countries, energy efficiency is a primary consideration in office design, and acoustic pods generally incorporate energy-saving features like LED lighting and motion sensors...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In France are acoustic pods from workwithisland.com energy efficient?',
            'country': 'France',
            'response': 'Acoustic pods from workwithisland.com available in France are designed with sustainability and energy efficiency as key features, aligning with French environmental standards...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In the UK what are the advantages of workwithisland.com acoustic booths?',
            'country': 'United Kingdom',
            'response': 'In the UK, workwithisland.com acoustic booths offer significant advantages including exceptional sound isolation, flexible placement, modern aesthetic design, and integration with digital tools...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In Spain how do workwithisland.com products integrate with office design?',
            'country': 'Spain',
            'response': 'In Spain, workwithisland.com products are designed to integrate seamlessly with modern office landscapes, offering flexible solutions that complement open-plan designs...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In Switzerland what materials are used in workwithisland.com acoustic pods?',
            'country': 'Switzerland',
            'response': 'Workwithisland.com acoustic pods available in Switzerland use premium materials including acoustic foam, sound-dampening fabrics, and environmentally sustainable wood products...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'In Benelux are workwithisland.com acoustic pods comfortable for extended use?',
            'country': 'Benelux',
            'response': 'In Benelux countries, workwithisland.com acoustic pods are designed for comfort during extended use, featuring ergonomic seating, appropriate ventilation, and adjustable lighting...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        }
    ]

    # Sample Personas data
    personas_data = [
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As a CEO how can acoustic solutions improve my company\'s productivity?',
            'country': 'France',
            'persona': 'CEO',
            'response': 'As a CEO, investing in acoustic solutions can significantly improve company productivity by reducing noise distractions that impact concentration and cognitive performance...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As an HR Manager what impact do acoustic pods have on employee wellbeing?',
            'country': 'United Kingdom',
            'persona': 'HR Manager',
            'response': 'As an HR Manager, you\'ll find that acoustic pods have a substantial positive impact on employee wellbeing by reducing noise stress, providing privacy for sensitive conversations, and offering spaces for mental breaks...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As an Interior Architect how do I integrate acoustic booths with office design?',
            'country': 'Spain',
            'persona': 'Interior Architect',
            'response': 'As an Interior Architect, integrating acoustic booths with office design requires thoughtful placement to complement traffic flow, visual harmony with the overall design language, and consideration of technical requirements...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As an Office Manager how quickly can acoustic pods be installed?',
            'country': 'Switzerland',
            'persona': 'Office Manager',
            'response': 'As an Office Manager, you\'ll be pleased to know that modern acoustic pods can typically be installed within 1-2 days with minimal disruption to the office environment...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As a Startup Founder what\'s the ROI for investing in acoustic solutions?',
            'country': 'Benelux',
            'persona': 'Startup Founder',
            'response': 'As a Startup Founder, the ROI for acoustic solutions comes from increased productivity, improved talent retention, enhanced company image, and more efficient use of office space...',
            'brand_mentioned': 'No',
            'visibule': 'No',
            'branded': 'No'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As a CEO are workwithisland.com acoustic pods worth the investment?',
            'country': 'France',
            'persona': 'CEO',
            'response': 'As a CEO, workwithisland.com acoustic pods represent a strategic investment that can deliver returns through improved employee productivity, enhanced company image, and flexible space utilization...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As an HR Manager how do workwithisland.com products affect employee satisfaction?',
            'country': 'United Kingdom',
            'persona': 'HR Manager',
            'response': 'As an HR Manager, workwithisland.com products have been shown to positively impact employee satisfaction by providing quiet spaces for focus, reducing noise stress, and demonstrating company investment in wellbeing...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As an Interior Architect what design options does workwithisland.com offer?',
            'country': 'Spain',
            'persona': 'Interior Architect',
            'response': 'As an Interior Architect, workwithisland.com offers a range of design options with customizable exteriors, various size configurations, and integration possibilities with existing design elements...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As an Office Manager how easy are workwithisland.com pods to maintain?',
            'country': 'Switzerland',
            'persona': 'Office Manager',
            'response': 'As an Office Manager, you\'ll find workwithisland.com pods are designed for easy maintenance with wipeable surfaces, replaceable components, and minimal technical upkeep requirements...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        },
        {
            'url': 'https://chatgpt.com/',
            'prompt': 'As a Startup Founder can workwithisland.com acoustic booths scale with my company?',
            'country': 'Benelux',
            'persona': 'Startup Founder',
            'response': 'As a Startup Founder, workwithisland.com acoustic booths are designed with scalability in mind, offering modular options that can be added to as your company grows...',
            'brand_mentioned': 'Yes',
            'visibule': 'Yes',
            'branded': 'Yes'
        }
    ]
    
    return france_data, countries_data, personas_data

def get_data():
    """
    For Vercel deployment, just return sample data
    """
    # In a serverless environment, we'll always use sample data
    return get_sample_data() 