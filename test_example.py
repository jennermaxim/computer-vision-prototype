"""
Example test script demonstrating all three tasks
Run this after setting up your API key
"""
from integrated_system import AILearningPlatform


def test_all_tasks():
    """Test all three tasks with examples"""
    
    platform = AILearningPlatform()
    
    print("\n" + "="*70)
    print("TESTING ALL THREE TASKS")
    print("="*70)
    
    # Task B & C: Text-based processing with classification
    print("\n" + "="*70)
    print("TASK (b) & (c): Text Processing + Classification")
    print("="*70)
    
    test_problems = [
        "our street is always flooded when it rains",
        "the school library has no books and the roof leaks",
        "people are getting sick from the contaminated water supply"
    ]
    
    for problem in test_problems:
        print(f"\n{'─'*70}")
        print(f"Problem: \"{problem}\"")
        print('─'*70)
        
        result = platform.process_text_description(problem)
        
        if result['success']:
            classification = result['classification']
            mission = result['mission_statement']
            
            print(f"\n✅ CLASSIFICATION:")
            print(f"   Category: {classification['category']}")
            print(f"   Confidence: {classification['confidence']}")
            
            print(f"\n🎯 MISSION STATEMENT:")
            print(f"   {mission['mission_statement']}")
            
            print(f"\n📋 ACTION STEPS:")
            for i, step in enumerate(mission.get('action_steps', [])[:3], 1):
                print(f"   {i}. {step}")
        else:
            print(f"❌ Error: {result.get('error')}")
        
        print()
    
    # Task A: Image processing (example with URL)
    print("\n" + "="*70)
    print("TASK (a): Computer Vision Detection")
    print("="*70)
    print("\nTo test image analysis, provide an image URL or path:")
    print("Example:")
    print("  result = platform.process_image('https://example.com/image.jpg')")
    print("  print(result['summary'])")
    
    print("\n" + "="*70)
    print("ALL TASKS DEMONSTRATED")
    print("="*70)


if __name__ == "__main__":
    test_all_tasks()
