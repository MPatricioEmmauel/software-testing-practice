# Dangerfile

# Method to check commit messages
def check_commit_messages
    git.commits.each do |commit|
      # Check if commit message title is more than 50 characters
      if commit.message.lines.first.chomp.length > 50
        fail("Commit title exceeds 50 characters: #{commit.sha}")
      end

      # Check if there's an empty line between title and description
      if commit.message.lines[1] && commit.message.lines[1].chomp != ""
        fail("Missing empty line after commit title: #{commit.sha}")
      end

      # Check if the description is at least 5 characters
      description = commit.message.lines[2..-1].join
      if description.length < 5
        fail("Commit description is less than 5 characters: #{commit.sha}")
      end

      # Check if each line in the description is more than 72 characters
      commit.message.lines[2..-1].each do |line|
        if line.chomp.length > 72
          fail("Line in commit description exceeds 72 characters: #{commit.sha}")
        end
      end
    end
  end

  # Run the method
  check_commit_messages
