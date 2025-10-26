"""
Main demonstration script for the AI-Powered Learning Platform
"""
import sys
from config import Config
from integrated_system import AILearningPlatform


def print_header(text: str):
    """Print a formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")


def demo_text_processing():
    """Demonstrate text-based problem processing"""
    print_header("TASK (b): NLP/LLM-based Mission Statement Generation")
    
    # Example problem descriptions
    problems = [
        "our street is always flooded when it rains",
        "the local clinic has no proper waiting area and people stand outside in the sun",
        "our school has broken desks and students have to share textbooks"
    ]
    
    platform = AILearningPlatform()
    
    for i, problem in enumerate(problems, 1):
        print(f"\n--- Example {i} ---")
        print(f"Original: \"{problem}\"")
        print("\nProcessing...\n")
        
        result = platform.process_text_description(problem)
        
        if result['success']:
            print(result['summary'])
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
        
        if i < len(problems):
            input("\nPress Enter to continue to next example...")


def demo_classification():
    """Demonstrate problem classification"""
    print_header("TASK (c): Problem Classification Engine")
    
    test_cases = [
        "The streets are filled with plastic waste and garbage",
        "Children in our school don't have enough desks to sit at",
        "The public hospital is overcrowded and lacks basic medical supplies",
        "Our river is polluted with industrial waste",
        "Teachers don't have proper teaching materials"
    ]
    
    platform = AILearningPlatform()
    
    print("Classifying various community problems:\n")
    
    for problem in test_cases:
        print(f"\nProblem: \"{problem}\"")
        print("Classifying...")
        
        result = platform.problem_classifier.classify_problem(problem)
        
        if result['success']:
            print(f"✅ Category: {result['category']}")
            print(f"   Confidence: {result['confidence']}")
            print(f"   Reasoning: {result['reasoning'][:150]}...")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
        
        print("-" * 70)


def demo_vision_processing():
    """Demonstrate computer vision processing"""
    print_header("TASK (a): Computer Vision Prototype")
    
    print("This system can detect community issues in images across multiple domains:")
    print("- Environment: littered streets, blocked drainage, deforestation, etc.")
    print("- Health: overcrowded clinics, unsanitary spaces, lack of safety gear, etc.")
    print("- Education: overcrowded classrooms, damaged infrastructure, etc.")
    
    print("\n" + "="*70)
    print("To test the vision detection, you can either:")
    print("1. Provide an image URL")
    print("2. Provide a local image path")
    print("="*70)
    
    # Example: You would provide actual image paths or URLs here
    print("\nExample usage (in code):")
    print("""
    platform = AILearningPlatform()
    
    # Using an image URL
    result = platform.process_image("https://example.com/image.jpg")
    
    # Or using a local image
    result = platform.process_image("/path/to/image.jpg")
    
    # The system will:
    # 1. Detect issues in the image
    # 2. Classify the problem
    # 3. Generate a mission statement
    print(result['summary'])
    """)


def interactive_mode():
    """Run the system in interactive mode"""
    print_header("Interactive Mode - AI Learning Platform")
    
    platform = AILearningPlatform()
    
    while True:
        print("\n" + "="*70)
        print("What would you like to do?")
        print("1. Analyze a problem description (text)")
        print("2. Analyze an image (URL or path)")
        print("3. Classify a problem")
        print("4. Generate mission statement only")
        print("5. Exit")
        print("="*70)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n📝 Enter a community problem description:")
            problem = input("> ").strip()
            if problem:
                result = platform.process_text_description(problem)
                if result['success']:
                    print(result['summary'])
                else:
                    print(f"❌ Error: {result.get('error')}")
        
        elif choice == '2':
            print("\n🖼️  Enter image URL or path:")
            image_path = input("> ").strip()
            if image_path:
                result = platform.process_image(image_path)
                if result['success']:
                    print(result['summary'])
                else:
                    print(f"❌ Error: {result.get('error')}")
        
        elif choice == '3':
            print("\n📊 Enter a problem to classify:")
            problem = input("> ").strip()
            if problem:
                result = platform.problem_classifier.classify_problem(problem)
                if result['success']:
                    print(f"\n✅ Category: {result['category']}")
                    print(f"   Confidence: {result['confidence']}")
                    print(f"   Reasoning: {result['reasoning']}")
                else:
                    print(f"❌ Error: {result.get('error')}")
        
        elif choice == '4':
            print("\n🎯 Enter a problem description:")
            problem = input("> ").strip()
            if problem:
                result = platform.mission_generator.generate_mission_statement(problem)
                if result['success']:
                    print(f"\n📋 Mission Statement:")
                    print(result['mission_statement'])
                    print(f"\n🎁 Expected Impact:")
                    print(result['expected_impact'])
                else:
                    print(f"❌ Error: {result.get('error')}")
        
        elif choice == '5':
            print("\n👋 Thank you for using the AI Learning Platform!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")


def main():
    """Main entry point"""
    print_header("AI-POWERED LEARNING PLATFORM")
    print("Recognizing and translating community challenges into learning missions")
    
    # Validate configuration
    try:
        Config.validate()
        print("✅ Configuration validated")
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("\nPlease set your OPENAI_API_KEY in the .env file")
        print("Copy .env.example to .env and add your API key")
        return
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'demo-all':
            demo_vision_processing()
            input("\nPress Enter to continue...")
            demo_text_processing()
            input("\nPress Enter to continue...")
            demo_classification()
        
        elif command == 'demo-vision':
            demo_vision_processing()
        
        elif command == 'demo-text':
            demo_text_processing()
        
        elif command == 'demo-classification':
            demo_classification()
        
        elif command == 'interactive':
            interactive_mode()
        
        else:
            print(f"Unknown command: {command}")
            print("\nAvailable commands:")
            print("  python main.py demo-all          - Run all demonstrations")
            print("  python main.py demo-vision       - Demo vision detection")
            print("  python main.py demo-text         - Demo text processing")
            print("  python main.py demo-classification - Demo classification")
            print("  python main.py interactive       - Interactive mode")
    
    else:
        print("\n" + "="*70)
        print("Available commands:")
        print("="*70)
        print("  python main.py demo-all          - Run all demonstrations")
        print("  python main.py demo-vision       - Demo vision detection (Task a)")
        print("  python main.py demo-text         - Demo text processing (Task b)")
        print("  python main.py demo-classification - Demo classification (Task c)")
        print("  python main.py interactive       - Interactive mode")
        print("="*70)
        print("\nOr run interactive mode by default...\n")
        
        interactive_mode()


if __name__ == "__main__":
    main()
